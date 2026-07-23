import os
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ API key not found.")
    exit()

# Initialize client
client = genai.Client(api_key=api_key)

# Read resume
reader = PdfReader("sample_resume.pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text

prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the following resume.

Provide:

1. ATS Score (/100)
2. Resume Summary
3. Technical Skills
4. Soft Skills
5. Missing Skills
6. Strengths
7. Weaknesses
8. Resume Improvements
9. Best Job Roles
10. Learning Roadmap

Resume:

{resume_text}
"""

try:
    response = client.models.generate_content(
       model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("\n========== AI RESUME ANALYSIS ==========\n")
    print(response.text)

except Exception as e:
    print("\n❌ Error while calling Gemini API")
    print(e)