# 📄 Smart CV Optimizer & ATS Scorer

## Overview
This project is an end-to-end application developed for the **Selected Topics** course at Almaarefa University. It uses an LLM (Google Gemini) to help job seekers optimize their CVs against specific Job Descriptions.

## 1. Idea & Problem Definition
* **Problem:** Applicants get rejected by ATS systems due to missing keywords.
* **Solution:** An AI app that analyzes the CV against the JD and suggests improvements.

## 2. UI/UX Design
* Built with **Streamlit** for a clean, side-by-side interface.

## 3. LLM Integration
* **API:** Google Gemini (`gemini-2.5-flash`).
* **Prompt:** Instructs the LLM to act as an ATS expert and output structured data.

## 4. Output Formatting
* The LLM is forced to output a **Markdown Table** and bullet points, rendered cleanly by Streamlit.

## 5. Responsible AI
* **Security:** API key is hidden in a `.env` file (Not hardcoded).
* **Error Handling:** Included checks for missing inputs and API connection errors.

## Team Members
* Student 1: [MESHAL ALDHAFEERU] - [212120771]
* Student 2: [Mishari Almaliki] - [212120668]