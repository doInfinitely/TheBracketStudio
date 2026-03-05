#!/usr/bin/env python3
"""
scan_projects.py — Anthropic-powered project scanner.

Scans GitHub, Vercel, Railway, GCP, Firebase, and AWS for projects,
checks live URLs, and uses Claude to generate structured project entries.

Usage:
    python3 scan_projects.py --mode new|append|update --format json|md --output projects.json
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic
import httpx

# Load .env file if present
_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    for line in _env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

ANTHROPIC_MODEL = "claude-sonnet-4-20250514"


# ═══════════════════════════════════════
# CLI SCANNERS
# ═══════════════════════════════════════

def run_cmd(cmd: list[str], timeout: int = 60) -> str:
    """Run a CLI command and return stdout, or error string."""
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
        if result.returncode != 0:
            return f"[ERROR] {' '.join(cmd)}: {result.stderr.strip()}"
        return result.stdout.strip()
    except FileNotFoundError:
        return f"[SKIPPED] {cmd[0]} not found"
    except subprocess.TimeoutExpired:
        return f"[TIMEOUT] {' '.join(cmd)}"


def scan_github() -> str:
    """Scan GitHub repos using gh CLI."""
    print("  Scanning GitHub...")
    repos = run_cmd([
        "gh", "repo", "list", "--limit", "200",
        "--json", "name,url,description,primaryLanguage,isPrivate,isFork,updatedAt,homepageUrl",
    ])
    return repos


def scan_vercel() -> str:
    """Scan Vercel projects."""
    print("  Scanning Vercel...")
    return run_cmd(["vercel", "project", "ls", "--json"], timeout=30)


def scan_railway() -> str:
    """Scan Railway projects."""
    print("  Scanning Railway...")
    return run_cmd(["railway", "list", "--json"], timeout=30)


def scan_gcloud() -> str:
    """Scan Google Cloud projects."""
    print("  Scanning Google Cloud...")
    projects = run_cmd(["gcloud", "projects", "list", "--format=json"], timeout=30)
    return projects


def scan_firebase() -> str:
    """Scan Firebase projects."""
    print("  Scanning Firebase...")
    return run_cmd(["firebase", "projects:list", "--json"], timeout=30)


def scan_aws() -> str:
    """Scan AWS resources."""
    print("  Scanning AWS...")
    parts = []

    # S3 buckets
    s3 = run_cmd(["aws", "s3", "ls"], timeout=30)
    parts.append(f"=== S3 Buckets ===\n{s3}")

    # EC2 instances
    ec2 = run_cmd([
        "aws", "ec2", "describe-instances",
        "--query", "Reservations[].Instances[].[InstanceId,State.Name,Tags[?Key=='Name'].Value|[0]]",
        "--output", "json"
    ], timeout=30)
    parts.append(f"=== EC2 Instances ===\n{ec2}")

    # Lambda functions
    lambdas = run_cmd([
        "aws", "lambda", "list-functions",
        "--query", "Functions[].[FunctionName,Runtime,LastModified]",
        "--output", "json"
    ], timeout=30)
    parts.append(f"=== Lambda Functions ===\n{lambdas}")

    return "\n\n".join(parts)


# ═══════════════════════════════════════
# SITE STATUS CHECKER
# ═══════════════════════════════════════

def check_site_status(url: str) -> str:
    """Check if a URL is up, down, or erroring."""
    try:
        with httpx.Client(timeout=10, follow_redirects=True) as client:
            # Try HEAD first
            try:
                resp = client.head(url)
            except httpx.HTTPError:
                resp = client.get(url)

            if 200 <= resp.status_code < 400:
                return "up"
            elif resp.status_code == 404:
                return "error"
            elif resp.status_code >= 500:
                return "down"
            else:
                return "error"
    except httpx.TimeoutException:
        return "down"
    except Exception:
        return "down"


def check_all_sites(projects: list[dict]) -> list[dict]:
    """Check site status for all projects with URLs."""
    print("\nChecking site status...")
    for project in projects:
        urls = project.get("urls", [])
        if urls:
            # Check the first URL as the primary
            url = urls[0].get("url", "")
            if url:
                status = check_site_status(url)
                project["site_status"] = status
                symbol = {"up": "+", "down": "!", "error": "x", "unknown": "?"}
                print(f"  [{symbol.get(status, '?')}] {url} -> {status}")
            else:
                project["site_status"] = "unknown"
        else:
            project["site_status"] = "unknown"
    return projects


# ═══════════════════════════════════════
# CLAUDE STRUCTURED EXTRACTION
# ═══════════════════════════════════════

EXTRACTION_PROMPT = """\
You are a project cataloger. Given raw CLI output from various cloud platforms \
(GitHub, Vercel, Railway, GCP, Firebase, AWS), extract and generate structured \
project entries.

For each project you can identify, produce a JSON object with this schema:
{
  "id": "kebab-case-id",
  "name": "Human Name",
  "subtitle": "Short tagline",
  "description": "1-3 sentence description of what the project does",
  "category": "flagship|ai-ml|tools|creative|web-social|education|research|other",
  "tech": ["Language1", "Framework1"],
  "platforms": ["GitHub", "Vercel"],
  "urls": [{"label": "example.com", "url": "https://example.com"}],
  "github_url": "https://github.com/...",
  "status": "live|deployed|in-development|research|functional|broken|offline|complete",
  "is_private": false,
  "is_fork": false,
  "primary_language": "TypeScript",
  "updated_at": "ISO-8601 timestamp",
  "site_status": "unknown"
}

Rules:
- Merge information across platforms (e.g., a GitHub repo deployed on Vercel)
- Use the repo description and name to infer what the project does
- Set category based on the project's purpose
- Use "live" for projects with working public URLs, "deployed" for cloud-hosted services, \
"in-development" for active WIP, "research" for academic/experimental, "functional" for \
complete but not deployed, "complete" for finished utilities, "broken" for 404/errors, \
"offline" for known-down services
- If a repo is a fork, set is_fork: true
- Include homepage URLs from GitHub if available
- Group related repos (e.g., frontend + backend) into single projects when obvious

Return ONLY a JSON array of project objects. No markdown, no explanation.\
"""


def extract_projects_with_claude(raw_data: dict) -> list[dict]:
    """Send raw platform data to Claude for structured extraction."""
    print("\nSending data to Claude for structured extraction...")

    client = anthropic.Anthropic()

    # Build the raw data message
    data_parts = []
    for platform, data in raw_data.items():
        data_parts.append(f"=== {platform.upper()} ===\n{data}")
    raw_text = "\n\n" + "\n\n".join(data_parts)

    message = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=16000,
        messages=[
            {
                "role": "user",
                "content": f"{EXTRACTION_PROMPT}\n\nHere is the raw platform data:\n{raw_text}",
            }
        ],
    )

    response_text = message.content[0].text.strip()

    # Parse JSON from response (handle possible markdown wrapping)
    if response_text.startswith("```"):
        lines = response_text.split("\n")
        # Remove first and last lines (```json and ```)
        lines = [l for l in lines if not l.strip().startswith("```")]
        response_text = "\n".join(lines)

    try:
        projects = json.loads(response_text)
        print(f"  Claude extracted {len(projects)} projects")
        return projects
    except json.JSONDecodeError as e:
        print(f"  ERROR: Failed to parse Claude response: {e}")
        print(f"  Response preview: {response_text[:500]}")
        return []


# ═══════════════════════════════════════
# MODE HANDLERS
# ═══════════════════════════════════════

def load_existing(path: str) -> list[dict]:
    """Load existing projects file."""
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def merge_new_only(existing: list[dict], scanned: list[dict]) -> list[dict]:
    """Return only projects not in existing data."""
    existing_ids = {p["id"] for p in existing}
    return [p for p in scanned if p["id"] not in existing_ids]


def merge_append(existing: list[dict], scanned: list[dict]) -> list[dict]:
    """Add new projects to existing list."""
    existing_ids = {p["id"] for p in existing}
    new = [p for p in scanned if p["id"] not in existing_ids]
    return existing + new


# ═══════════════════════════════════════
# OUTPUT FORMATTERS
# ═══════════════════════════════════════

def to_markdown(projects: list[dict]) -> str:
    """Convert projects list to markdown format."""
    lines = ["# Project Showcase — Remy Ochei\n"]

    # Group by category
    categories = {}
    for p in projects:
        cat = p.get("category", "other")
        categories.setdefault(cat, []).append(p)

    cat_titles = {
        "flagship": "Flagship Products",
        "ai-ml": "AI / Machine Learning",
        "tools": "Productivity & Utility Tools",
        "creative": "Creative / Media Tools",
        "web-social": "Web Apps & Social",
        "education": "Education & AI Tutoring",
        "research": "Research & Academic",
        "other": "Other",
    }

    for cat_key, title in cat_titles.items():
        cat_projects = categories.get(cat_key, [])
        if not cat_projects:
            continue

        lines.append(f"\n## {title}\n")
        for p in cat_projects:
            lines.append(f"### {p['name']} — {p['subtitle']}")
            lines.append(p["description"])
            lines.append("")
            if p["tech"]:
                lines.append(f"- **Tech:** {', '.join(p['tech'])}")
            if p["platforms"]:
                lines.append(f"- **Platforms:** {', '.join(p['platforms'])}")
            urls = p.get("urls", [])
            if urls:
                url_strs = [f"[{u['label']}]({u['url']})" for u in urls]
                lines.append(f"- **Live:** {', '.join(url_strs)}")
            lines.append(f"- **Status:** {p['status']}")
            if p.get("site_status") and p["site_status"] != "unknown":
                lines.append(f"- **Site Status:** {p['site_status']}")
            lines.append("\n---\n")

    return "\n".join(lines)


# ═══════════════════════════════════════
# MAIN
# ═══════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Scan platforms for projects and generate structured output."
    )
    parser.add_argument(
        "--mode",
        choices=["new", "append", "update"],
        default="update",
        help="new=only new projects, append=add new to existing, update=full rescan",
    )
    parser.add_argument(
        "--format",
        choices=["json", "md"],
        default="json",
        help="Output format",
    )
    parser.add_argument(
        "--output",
        default="projects.json",
        help="Output file path",
    )
    parser.add_argument(
        "--skip-scan",
        action="store_true",
        help="Skip platform scanning, only check sites on existing data",
    )
    parser.add_argument(
        "--check-sites",
        action="store_true",
        help="Check live site status for all project URLs",
    )
    args = parser.parse_args()

    # Check for API key
    if not args.skip_scan and not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    existing = load_existing(args.output)

    if args.skip_scan:
        # Just check sites on existing data
        if args.check_sites:
            projects = check_all_sites(existing)
        else:
            projects = existing
    else:
        # Run all platform scans
        print("Scanning platforms...")
        raw_data = {}

        scanners = {
            "github": scan_github,
            "vercel": scan_vercel,
            "railway": scan_railway,
            "gcloud": scan_gcloud,
            "firebase": scan_firebase,
            "aws": scan_aws,
        }

        for name, scanner in scanners.items():
            raw_data[name] = scanner()

        # Send to Claude for extraction
        projects = extract_projects_with_claude(raw_data)

        if not projects:
            print("No projects extracted. Exiting.")
            sys.exit(1)

        # Check site status if requested
        if args.check_sites:
            projects = check_all_sites(projects)

        # Apply mode
        if args.mode == "new":
            projects = merge_new_only(existing, projects)
            print(f"\nFound {len(projects)} new projects")
        elif args.mode == "append":
            projects = merge_append(existing, projects)
            print(f"\nTotal projects after append: {len(projects)}")
        else:  # update
            print(f"\nFull update: {len(projects)} projects")

    # Write output
    if args.format == "md":
        output_path = args.output if args.output.endswith(".md") else args.output.replace(".json", ".md")
        with open(output_path, "w") as f:
            f.write(to_markdown(projects))
        print(f"\nWrote {output_path}")
    else:
        output_path = args.output
        with open(output_path, "w") as f:
            json.dump(projects, f, indent=2)
        print(f"\nWrote {output_path} ({len(projects)} projects)")


if __name__ == "__main__":
    main()
