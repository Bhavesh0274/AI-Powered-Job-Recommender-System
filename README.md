# 💼 AI-Powered Job Recommender System

An end-to-end **AI-powered job recommendation system** that analyzes uploaded PDF resumes using **OpenAI GPT-3.5-Turbo**, extracts personalized job keywords, and fetches live job listings from **LinkedIn** and **Naukri** via **Apify actors** — all served through a **Streamlit** web interface. Also exposes job-fetching capabilities as an **MCP (Model Context Protocol) server** for agentic tool use.

---

## 🧠 Architecture Overview

```
User uploads PDF Resume (Streamlit UI)
            │
            ▼
┌──────────────────────────┐
│  PyMuPDF (fitz)          │  ── extracts raw text from PDF
└──────────────────────────┘
            │
            ▼
┌──────────────────────────────────────────────┐
│         OpenAI GPT-3.5-Turbo                 │
│                                              │
│  1. Resume Summarizer                        │
│     → skills, education, experience          │
│                                              │
│  2. Skill Gap Analyzer                       │
│     → missing certs, tools, experiences      │
│                                              │
│  3. Career Roadmap Generator                 │
│     → 3 career paths, roles, companies       │
│                                              │
│  4. Job Keyword Extractor                    │
│     → comma-separated job titles/keywords    │
└──────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────┐
│              Apify Platform                     │
│                                                 │
│  ┌─────────────────────┐  ┌──────────────────┐  │
│  │  LinkedIn Scraper   │  │  Naukri Scraper  │  │
│  │  (BHzefUZlZRKWxk..) │  │  (alpcnRV9YI9l..)│  │
│  │  top 60 live jobs   │  │  top 60 live jobs│  │
│  └─────────────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────┘
            │
            ▼
  Results rendered in Streamlit UI
  (title, company, location, direct link)

            +

┌──────────────────────────────┐
│   MCP Server (FastMCP)       │  ── exposes fetchlinkedin &
│   mcp_server.py              │     fetchnaukri as agent tools
└──────────────────────────────┘
```

---

## ✨ Key Features

- **PDF Resume Parser** — Extracts raw text from uploaded PDF resumes using **PyMuPDF (`fitz`)** with page-level iteration, enabling processing of multi-page resumes
- **Multi-prompt GPT Pipeline** — Sequentially calls GPT-3.5-Turbo for four distinct tasks: resume summarization, skill gap analysis, career roadmap generation, and job keyword extraction — each with tuned `max_tokens` budgets
- **Live Job Fetching via Apify** — Scrapes real-time job listings from **LinkedIn** (60 results) and **Naukri** (60 results) using Apify actors with residential proxy support, triggered dynamically from GPT-extracted keywords
- **Automated Keyword Extraction** — Derives the most relevant job titles and search terms directly from the resume summary using GPT, eliminating the need for manual keyword input
- **MCP Server Integration** — Exposes `fetchlinkedin` and `fetchnaukri` as async tools via **FastMCP**, enabling the job-fetching pipeline to be consumed directly by AI agents and LLM tool-use frameworks
- **Streamlit Web Interface** — Clean, styled UI with real-time spinners, markdown-rendered output cards, and a one-click "Get Job Recommendations" trigger for the full live-search pipeline

---

## 📁 Project Structure

```
AI-Powered-Job-Recommender-System/
├── app.py                  # Streamlit UI + full pipeline orchestration
├── mcp_server.py           # FastMCP server exposing job tools for agents
├── requirements.txt        # All dependencies
├── .env                    # API keys (not committed)
└── src/
    ├── helper.py           # PDF text extractor + OpenAI wrapper
    └── job_api.py          # Apify-based LinkedIn & Naukri job fetchers
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Bhavesh0274/AI-Powered-Job-Recommender-System.git
cd AI-Powered-Job-Recommender-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
APIFY_API_KEY=your_apify_api_key
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

### 5. (Optional) Run as MCP Server

```bash
python mcp_server.py
```

This starts the FastMCP server over `stdio`, exposing `fetchlinkedin` and `fetchnaukri` as agent-callable tools.

---

## 🔄 Pipeline Flow

| Step | Component | Description |
|------|-----------|-------------|
| 1 | `extract_text_from_pdf()` | Parses uploaded PDF resume page by page |
| 2 | `ask_openai()` — Summarize | Condenses resume into skills/experience overview |
| 3 | `ask_openai()` — Skill Gaps | Identifies missing tools, certs, and experiences |
| 4 | `ask_openai()` — Roadmap | Generates 3 career paths with roles and companies |
| 5 | `ask_openai()` — Keywords | Extracts job search keywords from summary |
| 6 | `fetch_linkedin_jobs()` | Calls Apify LinkedIn actor with extracted keywords |
| 7 | `fetch_naukri_jobs()` | Calls Apify Naukri actor with extracted keywords |
| 8 | Streamlit UI | Renders all results with job title, company, location, link |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | OpenAI GPT-3.5-Turbo |
| PDF Parsing | PyMuPDF (`fitz`) |
| Job Scraping | Apify (LinkedIn + Naukri actors) |
| Web Framework | Streamlit |
| MCP Server | FastMCP |
| Environment Config | python-dotenv |

---

## 🔮 Roadmap

- [ ] Add support for DOCX resume uploads
- [ ] Cache Apify results to reduce API costs on repeated queries
- [ ] Integrate more job platforms (Indeed, Internshala, Wellfound)
- [ ] Add ATS score calculator comparing resume against a job description
- [ ] Deploy on Streamlit Cloud with secure secrets management

---

## 👤 Author

**Bhavesh Nitin Bhadane**
M.Tech Dual Degree, IIT Kharagpur
📧 bhaveshbhadane.iitkgp@gmail.com | 🐙 [GitHub](https://github.com/Bhavesh0274)
