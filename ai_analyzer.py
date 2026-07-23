import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text):
    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the following resume.

Resume:
{resume_text}

Return:

1. ATS Score (0-100)
2. Resume Summary
3. Technical Skills
4. Soft Skills
5. Missing Skills
6. Strengths
7. Weaknesses
8. Resume Improvements
9. Suggested Job Roles
10. Final Recommendation
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
