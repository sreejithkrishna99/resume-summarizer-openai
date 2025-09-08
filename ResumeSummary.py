import os
import openai
from docx import Document
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# ========================
# CONFIGURATION
# ========================
# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_pdf(file_path):
    """Reads text from a PDF file."""
    pdf_reader = PdfReader(file_path)
    return " ".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())

def read_docx(file_path):
    """Reads text from a DOCX file."""
    doc = Document(file_path)
    return " ".join([para.text for para in doc.paragraphs if para.text.strip()])

def read_txt(file_path):
    """Reads text from a TXT file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_resume_text(file_path):
    """Extracts text from PDF, DOCX, or TXT resumes."""
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_path.endswith(".docx"):
        return read_docx(file_path)
    elif file_path.endswith(".txt"):
        return read_txt(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF, DOCX, or TXT.")

def summarize_resume(resume_text):
    """Uses OpenAI GPT API to summarize the resume."""
    prompt = f"""
    You are an AI assistant helping to summarize a candidate's resume for recruiters.

    Resume Content:
    {resume_text}

    Please generate a **professional summary** in 4-5 bullet points highlighting:
    - Candidate's overall experience
    - Technical skills & tools
    - Certifications (if any)
    - Notable achievements or projects

    Keep the tone **professional** and **concise**.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use GPT-3.5 for better speed and cost
        messages=[
            {"role": "system", "content": "You are an expert technical recruiter."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.3
    )

    return response.choices[0].message["content"]

if __name__ == "__main__":
    file_path = "Sreejith_Naveen_Resume.pdf"  # Change this to your resume file path

    try:
        resume_text = extract_resume_text(file_path)
        summary = summarize_resume(resume_text)

        print("\n===== PROFESSIONAL SUMMARY =====\n")
        print(summary)

    except Exception as e:
        print(f"❌ Error: {e}")
