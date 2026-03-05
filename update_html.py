#!/usr/bin/env python3
"""
update_html.py — Anthropic-powered HTML updater.

Reads projects.json and index.html, sends both to Claude API to update
the HTML project sections with new/changed projects while preserving
the existing Transistor/cyber aesthetic.

Usage:
    python3 update_html.py --input projects.json --html index.html
"""

import argparse
import json
import os
import sys
from pathlib import Path

import anthropic

# Load .env file if present
_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    for line in _env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

ANTHROPIC_MODEL = "claude-sonnet-4-20250514"

UPDATE_PROMPT = """\
You are an expert frontend developer. You will receive:
1. A JSON array of projects (the canonical data source)
2. The current index.html of a portfolio site

Your job: Update the HTML so the project sections reflect the JSON data.

CRITICAL RULES — you MUST follow all of these:
- Preserve the EXACT existing CSS, JavaScript, SVG circuit layer, header, \
profile card, nav, stats bar, experience section, education section, and footer. \
Do NOT modify any of these.
- Only modify the content inside the project <section> elements \
(#flagship, #ai-ml, #tools, #creative, and any new sections needed).
- Preserve the existing HTML structure, CSS classes, and card patterns exactly. \
Use the same class names: project-card, flagship, card-tag, card-title, \
card-desc, card-footer, card-tech, tech-chip, card-link, card-links, pulse-node, etc.
- For the card-tag, use these CSS classes based on status:
  - "live" → class="card-tag live" with <span class="pulse-node"></span>LIVE
  - "deployed" → class="card-tag deployed" with text DEPLOYED
  - "in-development" → class="card-tag dev" with text IN DEVELOPMENT
  - "research" → class="card-tag research" with text RESEARCH
  - "functional" → class="card-tag deployed" with text FUNCTIONAL
  - "broken" → class="card-tag broken" with text BROKEN
  - "offline" → class="card-tag broken" with text OFFLINE
  - "complete" → class="card-tag deployed" with text COMPLETE
- Flagship projects (category "flagship") go in #flagship with class="project-card flagship" \
and class="project-grid flagship"
- AI/ML projects go in #ai-ml
- Tools + web-social + education projects go in #tools
- Creative projects go in #creative
- Research and other categories can be omitted from the HTML (they're minor/archive projects)
- If a project has URLs, add card-links div with card-link anchors
- Include tech chips in card-footer for each technology
- Keep the section numbering (01, 02, 03, 04) and section headers intact
- The stats bar numbers should reflect the latest data if the project count has changed
- site_status "down" or "error" projects should still be shown but with appropriate status tags

Return ONLY the complete updated HTML. No markdown fences, no explanation. \
Start with <!DOCTYPE html> and end with </html>.\
"""


def update_html(projects_path: str, html_path: str, output_path: str | None = None):
    """Update HTML with project data using Claude."""

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    # Load inputs
    with open(projects_path, "r") as f:
        projects = json.load(f)
    with open(html_path, "r") as f:
        html_content = f.read()

    # Filter to only projects worth showing (skip minor archive/fork projects)
    shown_projects = [
        p for p in projects
        if not p.get("is_fork", False)
        and p.get("category") not in ("other",)
    ]

    print(f"Loaded {len(projects)} projects ({len(shown_projects)} to display)")
    print(f"HTML size: {len(html_content)} chars")

    client = anthropic.Anthropic()

    projects_json = json.dumps(shown_projects, indent=2)

    print("Sending to Claude for HTML update (streaming)...")
    updated_html = ""
    with client.messages.stream(
        model=ANTHROPIC_MODEL,
        max_tokens=32000,
        messages=[
            {
                "role": "user",
                "content": (
                    f"{UPDATE_PROMPT}\n\n"
                    f"=== PROJECTS JSON ===\n{projects_json}\n\n"
                    f"=== CURRENT INDEX.HTML ===\n{html_content}"
                ),
            }
        ],
    ) as stream:
        for text in stream.text_stream:
            updated_html += text
            print(".", end="", flush=True)
    print()
    updated_html = updated_html.strip()

    # Remove markdown fences if present
    if updated_html.startswith("```"):
        lines = updated_html.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        updated_html = "\n".join(lines)

    # Validate it looks like HTML
    if not updated_html.startswith("<!DOCTYPE") and not updated_html.startswith("<html"):
        print("WARNING: Response doesn't look like HTML. Saving raw response for inspection.")
        with open("update_html_debug.txt", "w") as f:
            f.write(updated_html)
        print("Saved to update_html_debug.txt")
        sys.exit(1)

    # Write output
    out = output_path or html_path
    with open(out, "w") as f:
        f.write(updated_html)
    print(f"Updated HTML written to {out} ({len(updated_html)} chars)")


def main():
    parser = argparse.ArgumentParser(
        description="Update portfolio HTML from projects JSON using Claude."
    )
    parser.add_argument(
        "--input",
        default="projects.json",
        help="Path to projects JSON file",
    )
    parser.add_argument(
        "--html",
        default="index.html",
        help="Path to index.html to update",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output path (defaults to overwriting --html)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write to index_updated.html instead of overwriting",
    )
    args = parser.parse_args()

    output = args.output
    if args.dry_run and not output:
        base = os.path.splitext(args.html)[0]
        output = f"{base}_updated.html"

    update_html(args.input, args.html, output)


if __name__ == "__main__":
    main()
