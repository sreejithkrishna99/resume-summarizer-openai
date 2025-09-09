# Resume Summarizer using OpenAI GPT

A Python project that automatically summarizes resumes using the **OpenAI GPT API (old SDK)**.  
Supports **PDF, DOCX, and TXT** formats and generates a concise professional summary in 4–5 bullet points.

---

## Features

- Extract text from **PDF, DOCX, and TXT** resume files.
- Summarizes resumes using **GPT-3.5-turbo**.
- Highlights:
  - Candidate's overall experience
  - Technical skills & tools
  - Certifications
  - Notable achievements/projects
- Generates output in a **professional and concise** format.

---

## Requirements

- Python 3.8+
- [OpenAI Python SDK (v0.28)](https://pypi.org/project/openai/0.28/)
- python-docx
- PyPDF2
- python-dotenv

---

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


2. Create and Activate a Virtual Environment (Recommended)

Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Your OpenAI API Key

Create a .env file in the project folder:
OPENAI_API_KEY=your_openai_api_key_here

5. Place Your Resume File

Put your resume in the project folder (.pdf, .docx, or .txt) and edit the file_path variable in ResumeSummary.py:
file_path = "Your_Resume.pdf"

6. Run the Script
python ResumeSummary.py

Example Output
<img width="1430" height="291" alt="image" src="https://github.com/user-attachments/assets/6a27024c-3f4b-4dfe-b663-0427d0a64e91" />




