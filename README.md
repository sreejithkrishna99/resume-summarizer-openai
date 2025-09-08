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

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2. Create and Activate a Virtual Environment (Recommended)
Windows:

bash
Copy code
python -m venv venv
venv\Scripts\activate
Mac/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
Or, if you don’t have a requirements.txt yet, install manually:

bash
Copy code
pip install openai==0.28 python-docx PyPDF2 python-dotenv
4. Set Up Your OpenAI API Key
Create a .env file in the project folder:

ini
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Important: Do not commit your .env file to GitHub.
Use .env.example as a placeholder.

5. Place Your Resume File
Put your resume in the project folder (.pdf, .docx, or .txt) and edit the file_path variable in ResumeSummary.py:

python
Copy code
file_path = "Your_Resume.pdf"
6. Run the Script
bash
Copy code
python ResumeSummary.py
The professional summary will appear in the console.

Example Output

Replace screenshot.png with your actual screenshot of the program output.

Project Structure
Copy code
ResumeSummarizer/
│
├─ ResumeSummary.py
├─ requirements.txt
├─ .env.example
├─ README.md
└─ screenshot.png
License
MIT License © [Your Name]
