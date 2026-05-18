📄 Smart CV Optimizer & ATS Scorer Pro

An advanced end-to-end application developed as part of the Selected Topics course at Almaarefa University (Computer Science and Information Systems Department). This tool harnesses the power of Google Gemini LLM to parse resumes, analyze compliance against Job Descriptions (JDs), evaluate ATS matching scores, and provide pro-level career assistance.

🚀 Key Upgrades in Pro Version

Interactive File Uploads: Supports parsing text directly from .pdf and .docx format files.

Visual Dashboard: Beautiful Custom HTML/CSS styled circular score indicator and colorful metric pills representing matched (green) and missing (red) keywords.

Try Demo Feature: Quick load button which populates sample data for instant demonstration to the grading committee.

Bilingual Support: High-fidelity UI available in both English and Arabic with a toggle.

AI Cover Letter Generator: Auto-generates matching professional application letters.

Smart Interview Simulator: Tailors 3 contextual interview prep questions targeting the gaps found in the user's CV.

📈 Evaluation Framework Alignment

1. Idea & Problem Definition (10%)

Problem: Over 75% of job applications are filtered out by automated Applicant Tracking Systems (ATS) due to poor formatting or missing core competencies.

LLM Value-Add: Leverages Large Language Model reasoning to extract semantic skills, weights, gaps, and optimize resumes dynamically.

2. UI/UX Design (20%)

Framework: Powered by Streamlit.

Design Philosophy: Clean, premium, dark-themed SaaS-like look utilizing responsive structures, visual status metrics, tab navigations, and clear callouts.

3. LLM Integration & Prompt Design (20%)

Model Engine: Google Gemini API (gemini-2.5-flash).

Prompt Engineering: Uses structured JSON Schema instructions enforcing strict compliance with JSON response formats, preventing unformatted or verbose paragraphs.

4. Output Formatting (20%)

Standardizes all raw output into structured JSON, allowing the code to parse metrics, arrays of strings, and objects to render visual elements natively (progress cards, expandable interview blocks).

5. Responsible AI Practices

Secret Management: Utilizes .env environments and ignores confidential API tokens from source control via .gitignore.

Robust Error Handling: Employs defensive validation ensuring no system crashes occur upon network outages, wrong file parses, or empty string submissions.

🛠️ Step-by-Step Installation Guide

Clone the repository:

git clone [https://github.com/meshaldhafeeri/CV-Optimizer-AI.git](https://github.com/meshaldhafeeri/CV-Optimizer-AI.git)
cd CV-Optimizer-AI


Install requirements:

pip install -r requirements.txt


Configure API Key:
Create a .env file in the root directory and write your Google Gemini API key:

GEMINI_API_KEY=AIzaSy...your_actual_api_key_here


Run Web App:

python -m streamlit run app.py


👥 Project Team Credits

Student 1 (Lead Developer): Meshal - 212120771

Student 2 (Research & Presentation): Mishari - 212120668