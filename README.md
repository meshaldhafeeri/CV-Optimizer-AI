# Smart CV Optimizer & ATS Scorer Pro

An advanced end-to-end application developed as part of the Selected Topics course at Almaarefa University (Computer Science and Information Systems Department). This tool harnesses the power of Google Gemini LLM to parse resumes, analyze compliance against Job Descriptions (JDs), evaluate ATS matching scores, and provide pro-level career assistance.

## Key Upgrades in Pro Version (Startup MVP)
* **Explainable Deterministic Scoring:** A mathematical Python-based engine that evaluates skills, action verbs, and structure with full transparency (Explainable AI), rather than relying on LLM hallucinations.
* **AI Recruiter Simulation:** Generates a brutally honest, human-like recruiter impression and calculates the estimated interview probability.
* **Bilingual & Arabic-First Engine:** High-fidelity UI available in both English and Arabic, specifically optimized to parse and understand local market requirements.
* **Smart AI Rewrite Coach:** Auto-detects weak bullet points in the resume and proposes impactful, metric-driven alternatives.
* **Try Demo Feature:** Quick load button which populates an enterprise-grade sample profile (Senior Backend Engineer) for instant demonstration to the grading committee.

## Evaluation Framework Alignment

**1. Idea & Problem Definition (10%)**
* **Problem:** Over 75% of job applications are filtered out by automated Applicant Tracking Systems (ATS) due to poor formatting, lack of measurable metrics, or missing core competencies.
* **LLM Value-Add:** Leverages Large Language Model reasoning to extract semantic skills, weights, gaps, and optimize resumes dynamically without breaking data privacy.

**2. UI/UX Design (20%)**
* **Framework:** Powered by Streamlit.
* **Design Philosophy:** Clean, premium, dark-themed SaaS-like look utilizing responsive structures, visual SVG Gauge metrics, tab navigations, and clear glass-morphism cards.

**3. LLM Integration & Prompt Design (20%)**
* **Model Engine:** Google Gemini API (gemini-2.5-flash).
* **Prompt Engineering:** Uses structured JSON Schema instructions enforcing strict compliance with JSON response formats, separating data extraction from scoring logic.

**4. Output Formatting (20%)**
* Standardizes all raw output into structured JSON, using robust fail-safe parsing mechanisms (Regex Fallbacks) to render visual elements natively (progress cards, pills, explainable scoreboards).

**5. Responsible AI Practices**
* **Secret Management:** Utilizes `.env` environments and ignores confidential API tokens from source control via `.gitignore`.
* **Robust Error Handling:** Employs defensive validation ensuring no system crashes occur upon network outages, wrong file parses, or LLM hallucination limits.

## Step-by-Step Installation Guide

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/meshaldhafeeri/CV-Optimizer-AI.git](https://github.com/meshaldhafeeri/CV-Optimizer-AI.git) 
   cd CV-Optimizer-AI
