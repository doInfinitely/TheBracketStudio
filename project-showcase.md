# Project Showcase — Remy Ochei

## Flagship Products

### Rho-Bot — Autonomous Desktop Agent
An autonomous desktop agent that automates computer tasks by observing user behavior, learning goals, and executing actions through clicks and keystrokes. Decomposes user objectives into hierarchical plans and executes them locally — a cheaper alternative to LLM-based computer automation.

- **Tech:** TypeScript, Python
- **Platforms:** GitHub, Vercel, Railway (Postgres)
- **Live:** [rho-bot.net](https://rho-bot.net)
- **Status:** Live, early access with pricing plans and downloads

---

### CloudRun — Compliance-First Last-Mile Delivery Marketplace
An age-restricted delivery marketplace (Model A, Texas-first) connecting merchants, customers, and drivers for regulated products. Features intelligent dispatch orchestration (FAST + BATCH algorithms), real-time tracking, age/ID verification, H3 geospatial indexing, OSRM routing, and full compliance infrastructure. FastAPI backend with 50+ endpoints, Celery workers, and four React storefronts.

- **Tech:** JavaScript/TypeScript, Python (FastAPI)
- **Platforms:** GitHub, Vercel (5 apps), Railway (Postgres + Redis), GCP
- **Live:**
  - [cloudrun.shop](https://cloudrun.shop) (marketing)
  - [app.cloudrun.shop](https://app.cloudrun.shop) (customer)
  - [merchant.cloudrun.shop](https://merchant.cloudrun.shop) (merchant)
  - [drive.cloudrun.shop](https://drive.cloudrun.shop) (driver)
  - [admin.cloudrun.shop](https://admin.cloudrun.shop) (admin/mission control)
- **Status:** Live, launching in Texas. All sub-apps deployed and functional.

---

### TravelPal — Gamified Location-Based Experience Platform
A monorepo containing three React apps (FlavorAtlas, QuestLog, PhantomNav) sharing a Firebase backend and ~24 shared modules. Each app skins the same core concept — discovering and collecting real-world places — with a different video game aesthetic (Palia, Genshin Impact, Persona 5). Think Pokedex meets Yelp meets gacha games.

- **Tech:** TypeScript (React), Firebase
- **Platforms:** GitHub, Vercel (3 apps), Railway, Firebase (3 web apps), GCP (2 projects)
- **Live:**
  - [phantomnav.vercel.app](https://phantomnav.vercel.app) (PhantomNav)
  - [flavoratlas.vercel.app](https://flavoratlas.vercel.app) (FlavorAtlas)
  - [questlog-remy-ocheis-projects.vercel.app](https://questlog-remy-ocheis-projects.vercel.app) (QuestLog)
- **Status:** Deployed, functional SPAs

---

### SparkSeekr — Companionship App
A companionship app where Seekers find their Muse.

- **Tech:** TypeScript
- **Platforms:** GitHub, Vercel (2 deployments), GCP (2 projects), custom domains (sparkseekr.com/.net/.org)
- **Live:** [sparkseekr.com](https://sparkseekr.com) — currently down (DNS not resolving)
- **Status:** Deployed but currently offline

---

## AI / Machine Learning

### Tiny OCR — Specialized STEM OCR Service
A specialized OCR service that converts images of math equations, chemical structures, handwriting, and documents into structured text (LaTeX, SMILES, Markdown). Targets researchers, chemists, educators, and developers with sub-50ms latency and 99.7% accuracy on STEM content.

- **Tech:** TypeScript (frontend), Python (backend)
- **Platforms:** GitHub, Vercel, GCP
- **Live:** [tiny-ocr.com](https://tiny-ocr.com)
- **Status:** Live and working with interactive demo, pricing tiers, and API docs

---

### Tiny Tessarachnid — Simplified Modern Tesseract OCR
A simplified modern implementation of Tesseract OCR. The core model powering the tiny-ocr service, glyph-daemon, and related OCR projects.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete, foundational library for the OCR ecosystem

---

### Glyph Daemon — Encrypted OCR Inference Backend
Encrypted inference backend for the tiny-tessarachnid OCR models. Serves three model versions (RetinaOCRNet, RetinaOCRGPT, ContourOCRNet) behind a FastAPI endpoint with AES-256 encrypted weights that decrypt into memory at boot.

- **Tech:** Python (FastAPI)
- **Platforms:** GitHub, Railway
- **Status:** Deployed on Railway, operational

---

### Winnie Interface — RLHF Annotation Rater
Web interface for rating OCR bounding-box annotations for the tiny-tessarachnid pipeline. Shows document images alongside interactive SVG bounding-box overlays at four hierarchical levels with Good/Bad rating buttons for human feedback.

- **Tech:** TypeScript
- **Platforms:** GitHub, Vercel, GCP
- **Live:** [winnie-interface.vercel.app](https://winnie-interface.vercel.app)
- **Status:** Deployed, functional annotation tool

---

### Nissl — Hierarchical Detection + Infill Network
Extends the tiny-tessarachnid OCR architecture with a masked infill head that proves the model understands detected content by reconstructing it from surrounding context. Uses ResNet encoder with autoregressive detection and U-Net decoder for pixel reconstruction.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Research/experimental

---

### Macrodose — macOS Behavior Logger & Action Predictor
A macOS behaviour logger and hierarchical action-prediction model. Captures mouse clicks, keyboard events, screenshots, and the accessibility tree at every event, then trains a model that predicts the next user action by auto-regressively zooming through the UI hierarchy.

- **Tech:** Python
- **Platforms:** GitHub, AWS (S3)
- **Status:** In development, data collection and model training infrastructure built

---

### Mangaka — Hierarchical Manga Analysis & Generation
Converts manga pages into structured JSON representations and back into images through four stages: cloud annotation with vision LLMs (Claude, GPT-4o, Gemini), local model training (GPT-2 + Stable Diffusion), distillation loop, and dataset generation for RAG/finetuning.

- **Tech:** Python
- **Platforms:** GitHub, Railway
- **Status:** Pipeline functional, research/experimental

---

### Musepix — Music/Sheet Music OCR
A retina-based hierarchical detector for sheet music images. Detects and recognizes musical elements with audio OCR, MIDI decoding, symbol similarity models, and OpenAI-based annotation.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Research/experimental

---

### Handwriting Orca Math — Handwriting Recognition
Handwriting recognition system for mathematical content.

- **Tech:** TypeScript
- **Platforms:** GitHub, Railway, GCP
- **Status:** Deployed on Railway

---

### Room Detection — AI Room/Photo Classification
Room detection and classification from photos. Full AWS infrastructure with EC2 instance, Lambda functions, ECS cluster, and S3 storage. Deployed via CloudFormation and SAM CLI.

- **Tech:** Python
- **Platforms:** GitHub, AWS (EC2, Lambda x2, ECS, S3 x3, CloudFormation)
- **Status:** Infrastructure deployed, EC2 instance currently stopped (since Feb 9, 2026)

---

### Hierarchical Goal Induction — Research Paper
Academic research on hierarchical goal induction.

- **Tech:** TeX
- **Platform:** GitHub
- **Status:** Research paper/document

---

### Every Noise — Music Genre Classifier
Scrapes genre-to-artist mappings from Every Noise at Once and Spotify, downloads music, maps artists to YouTube, and trains a music genre classifier.

- **Tech:** Python
- **Platforms:** GitHub, AWS (S3)
- **Status:** Data pipeline built, classifier in development

---

### Selective Speaker — Voice App
Voice/speaker-related application with a registered Firebase Android app.

- **Tech:** Python
- **Platforms:** GitHub, Firebase (Android app), GCP
- **Status:** Built

---

### Browser-Use Travel Agent Benchmark
A benchmark suite for evaluating AI agents that use browsers to complete travel-related tasks. Includes categorized tasks, a runner, and report generation.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete benchmark tool

---

## Data Analysis & Investigation

### Epsteinalysis — Epstein Document Analysis Platform
A document analysis and investigation platform for exploring ~1.05 million documents (2.08 million pages) related to the Epstein case. Provides browsing, searching, timeline views, network analysis, entity exploration, and image/video analysis.

- **Tech:** Python (backend), TypeScript (frontend)
- **Platforms:** GitHub, Vercel, AWS (S3), GCP
- **Live:** [epsteinalysis.com](https://epsteinalysis.com)
- **Status:** Live and fully working with multiple operational sections

---

### Project Icarus — AI Agent for Epstein Story Discovery
A Python CLI tool using Anthropic Claude to discover and publish stories from the Epstein files via Reddit (PRAW) and Twitter (Tweepy).

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Functional CLI tool

---

### Epstein Corollary
Related analysis/tooling for the Epstein investigation.

- **Tech:** Python
- **Platforms:** GitHub, GCP (the-corollary-system)
- **Status:** Supplementary project

---

### Elonalysis — Elon Musk Sentiment Analysis
A real-time sentiment analysis and fact-checking platform that monitors public perception of Elon Musk across X/Twitter, Reddit, YouTube, news sites, and Hacker News. Tracks sentiment trends, verifies claims, monitors promises, and analyzes how events impact public opinion.

- **Tech:** TypeScript
- **Platforms:** GitHub, Vercel
- **Live:** [elonalysis.vercel.app](https://elonalysis.vercel.app)
- **Status:** Live and working with active sentiment tracking

---

## Creative / Media Tools

### Black Ringo — AI Comic Generator
Paste links to comics and it generates a brand new comic in their combined style. Built with Next.js 14, TypeScript, Tailwind CSS, and Framer Motion.

- **Tech:** TypeScript
- **Platforms:** GitHub, GCP
- **Status:** In development

---

### Video Generation Pipeline
AI-powered video generation for educational/explanatory videos. Takes a text prompt, uses an LLM for storyboard generation, splits into 6-second chunks, generates each with Minimax video-01, and stitches with FFmpeg.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Functional pipeline

---

### Spleeterino — Neural Music Generator
LSTM-based music generation tool that predicts mel spectrogram frames from training audio, then generates new music autoregressively. Can stream output or save to WAV.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Functional

---

### Turntable — 3D Voxel Reconstruction from Video
Takes turntable/orbit videos and reconstructs 3D voxel models through reconstruction, subdivision, and differentiable flow-based hardening. Supports multi-GPU processing, interactive viewers, and PLY export.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Functional, runs on Lambda GPU cloud

---

### Ars Chorda — Music Theory Tool
Music theory and chord-related Python tool.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Live2D Web
Live2D character rendering for the web.

- **Tech:** HTML/JavaScript
- **Platform:** GitHub
- **Status:** Functional

---

### Face Rig (Watercolor Rig)
Visual/creative tool for character rigging or watercolor-style rendering.

- **Tech:** JavaScript
- **Platform:** Vercel
- **Live:** [face-rig.vercel.app](https://face-rig.vercel.app)
- **Status:** Deployed

---

## Productivity & Utility Tools

### Spindle — AI Chat Agent with 3D Graph Visualization
An AI chat agent that visualizes web traversal in a live 3D force-directed graph as it searches and browses pages to answer questions. Supports OpenAI and Anthropic LLMs with Tavily web search.

- **Tech:** TypeScript
- **Platform:** GitHub
- **Status:** In development

---

### Claude Cursor — Web Terminal Session Manager
A web-based terminal session manager for running and juggling multiple Claude Code sessions. Uses ttyd + tmux for persistent terminal sessions accessible from any browser.

- **Tech:** JavaScript
- **Platform:** GitHub
- **Status:** Functional

---

### Audio Out Transcription (Air Traffic Control)
macOS system audio transcription tool with forced alignment. Captures system audio via ScreenCaptureKit, transcribes with Whisper and forced alignment (praatio). Features a PyQt6 GUI.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Functional

---

### Gmail Job Filter
Automated Gmail filtering for job-related emails.

- **Tech:** Python
- **Platforms:** GitHub, Railway, GCP
- **Status:** Deployed on Railway

---

### Frank Invoice Processor
AI-powered invoice processing app. Upload PDF invoices and GPT-4o extracts structured data with real-time reactive UI updates. Built with Nuxt 3, Vue 3, and Convex.

- **Tech:** TypeScript
- **Platform:** GitHub
- **Status:** Functional

---

### Spend Sense — Expense Tracker
Personal expense tracking and financial management tool.

- **Tech:** JavaScript
- **Platform:** GitHub
- **Status:** Built

---

### Clip Forge — Video Clip Editor
Video clip editing tool.

- **Tech:** JavaScript
- **Platform:** GitHub
- **Status:** Built

---

### ISBN Lookup
A small project for looking up and working with ISBNs.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Get Pronunciations
Fetches pronunciation audio files from dictionary.com.

- **Tech:** Shell
- **Platform:** GitHub
- **Status:** Complete utility

---

### UwU Filter
A text "uwu-ification" filter that progressively degrades text into uwu-speak with replaced letters, emoticons, and degraded grammar.

- **Tech:** Shell
- **Platform:** GitHub
- **Status:** Complete, novelty tool

---

### Kindling — Amazon Book Research Tool
Amazon book research and content extraction tool. Uses Selenium, pyautogui, and pytesseract for web scraping Amazon nonfiction categories, cross-referencing book ideas, and generating book content.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Built

---

## Web Apps & Social

### Collab Canvas — Collaborative Drawing App
A collaborative canvas/drawing application with real-time collaboration, sign-in, and shared workspace dashboard. Built with Next.js and Supabase.

- **Tech:** TypeScript
- **Platforms:** GitHub, Vercel
- **Live:** [collab-canvas-vert.vercel.app](https://collab-canvas-vert.vercel.app)
- **Status:** Live and working

---

### Curio — Visual Discovery Platform for Smoke Shop
Two products sharing a Supabase backend: a public Next.js website with dynamically reconfiguring masonry layout for a smoke shop, and a private React Native/Expo owner app for inventory management.

- **Tech:** TypeScript
- **Platforms:** GitHub, Railway (3 projects)
- **Status:** Deployed on Railway, multi-service

---

### Concord — Messaging App
A Discord and Slack inspired messaging app with an extensive cloud backend. Features AI services, intelligent search, priority checking, conflict resolution, proactive AI assistant, and push notifications.

- **Tech:** Swift (iOS)
- **Platforms:** GitHub, Firebase (iOS app), GCP (7 Cloud Run services, 7 Cloud Functions)
- **Cloud Run Services:**
  - aiService, intelligentSearch, checkPriority, checkConflictsAndSuggest, proactiveAssistant, sendMessageNotification, sendGroupAddedNotification
- **Status:** Built with full backend infrastructure

---

### Deaddit — Blogging Platform
A basic blogging platform with a Markdown editor for creating posts and a viewer for reading them.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Presence App — Online Status Tracker
An app that shows who's online and who's offline.

- **Tech:** TypeScript
- **Platform:** GitHub
- **Status:** Built

---

### Auth Minimal — Authentication Starter
A minimalist authentication app with user sign-in and protected dashboard. Built with Next.js and Supabase.

- **Tech:** TypeScript
- **Platforms:** GitHub, Vercel
- **Live:** [auth-minimal.vercel.app](https://auth-minimal.vercel.app)
- **Status:** Live and working

---

## Education & AI Tutoring

### AI Study Companion
An interactive educational chatbot with a customizable animated avatar companion. Users converse with an AI assistant designed for learning support while personalizing the avatar's appearance.

- **Tech:** HTML/TypeScript
- **Platforms:** GitHub, Vercel
- **Live:** [ai-study-companion-beryl.vercel.app](https://ai-study-companion-beryl.vercel.app)
- **Status:** Live and working

---

### AI Math Tutor
An AI math tutoring application that lets users upload images and interact with an AI assistant for mathematical help.

- **Tech:** TypeScript
- **Platforms:** GitHub, Vercel
- **Live:** [ai-math-tutor-xi.vercel.app](https://ai-math-tutor-xi.vercel.app) — returns 404
- **Status:** Broken (404 error)

---

### Seed of Athena — Adaptive Question Generator
"If you could only ask one question to assay all your students what would it be? But you must not demoralize them..." An adaptive/optimal question generation system for student assessment.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Research/concept

---

## Backend Services

### Swiftora — Web App
Web application with Firebase and Railway backend.

- **Tech:** Web
- **Platforms:** Firebase (web app), Railway, GCP (2 projects)
- **Status:** Backend deployed on Railway

---

### Alexa ANFE — Cloud Run Service
Cloud Run service deployed on Google Cloud.

- **Tech:** Unknown
- **Platform:** GCP (Cloud Run)
- **Live:** [alexa-anfe-app](https://alexa-anfe-app-18169467774.us-central1.run.app)
- **Status:** Deployed (last deployed Dec 14, 2025)

---

### Marionette
GCP project with unknown purpose.

- **Platform:** GCP
- **Status:** Project created, no active compute services detected

---

## 3D / Game Development

### Voxel Editor
A 3D voxel editor.

- **Tech:** C++
- **Platform:** GitHub
- **Status:** Built

---

### SandPond — 3D Atom Engine
A 3D atom simulation engine.

- **Tech:** JavaScript
- **Platform:** GitHub
- **Homepage:** [sandpond.cool](https://www.sandpond.cool)
- **Status:** Built

---

### Pi Point
Point-of-sale or utility application.

- **Tech:** TypeScript
- **Platform:** GitHub
- **Status:** Built

---

## Benchmarks & Assessments

### Mati AIChamp — RL Environment Engineer Assessment
Take-home assessment for an RL Environment Engineer role.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Visual Concepts — Game Studio Assessment
Take-home assignment for Visual Concepts Game Studios.

- **Tech:** C++
- **Platform:** GitHub
- **Status:** Complete

---

### Postera Remy — Drug Discovery Assessment
Take-home assignment in Jupyter Notebook format.

- **Tech:** Jupyter Notebook
- **Platform:** GitHub
- **Status:** Complete

---

### Simplified Rocket Lab Puzzle
A puzzle based on Little Rocket Lab for LLMs.

- **Platform:** GitHub
- **Status:** Complete

---

## Research & Academic

### Academic Writing Portfolio
Academic writing by Remy Ochei in Math and Science.

- **Platform:** GitHub
- **Status:** Archive

---

### Force-Directed Graph Engine
A local, collision-based model of electromagnetism developed to compute force-directed graphs.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### GPU-Accelerated CNN Study
A study in implementing GPU-accelerated convolutional neural networks.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Feedforward Neural Net Study
A simple study of feedforward neural nets in Python.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Neural Levenshteiner
Neural network approach to Levenshtein distance computation.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Research project

---

### Suggest HCPCS
Baseline models for matching medical descriptions to their HCPCS codes.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Decision Tree Study
Machine learning study on decision trees.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### MNIST Flax
Simple MNIST training using Flax and JAX.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Multivariate Linear Regression Study
Machine learning regression study.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

### Van Scheduling — CSCE 5210
Van scheduling optimization project for CSCE 5210 course.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete coursework

---

### Stochastic Rounding
Stochastic rounding implementation and study.

- **Tech:** Python
- **Platform:** GitHub
- **Status:** Complete

---

## Other

| Project | Description | Tech | Status |
|---------|-------------|------|--------|
| AmazonMonitor | Amazon price/stock checker Discord bot | JavaScript | Fork |
| Monome | Music controller interface | Python | Built |
| Dice Game | Python dice game | Python | Complete |
| Manga Translate | Manga translation tool | Python | Built |
| Python Image Character Generator | Character image generation | Python | Built |
| MNIST Helpers | MNIST utility scripts | Python | Complete |
| MaxDiffusion | Diffusion model study | Python | Fork |
| Neural Voice Cloning | Few-shot voice cloning | Python | Fork |
| MT-DNN | Multi-task deep neural networks for NLU | Python | Fork |
| Zed | High-performance code editor | Rust | Fork |
| Godot | Multi-platform game engine | C++ | Fork |
| Pygames | Python game collection | Python | Built |
| Yandex Data Science Tutor | Tutoring assignment | HTML | Complete |
| Sakuraba Noise Pack | Audio noise pack | N/A | Asset pack |
| Library of Rho | Collection of mathematical/scientific texts | N/A | Archive |
| Chegg Tutoring Portfolio | Sample tutoring assignments (Fall 2019) | JavaScript | Archive |
| Mr Automate | Automation tool | Python | Built |
| Find Subimage | Subimage detection tool | Python | Built |
| DoltHub Data | Data bounty contribution | N/A | Complete |

---

## Platform Summary

| Platform | Projects | Active Deployments |
|----------|----------|-------------------|
| **GitHub** | 97 repos (74 public, 23 private) | — |
| **Vercel** | 19 projects, 9 custom domains | ~14 live sites |
| **Railway** | 12 projects | Multiple services with Postgres/Redis |
| **Google Cloud** | 22 projects | 8 Cloud Run services, 9 Cloud Functions |
| **Firebase** | 5 projects | 6 apps (1 iOS, 1 Android, 4 Web) |
| **AWS** | 1 main project + 4 data buckets | EC2 (stopped), 2 Lambdas, 1 ECS cluster, 8 S3 buckets |
