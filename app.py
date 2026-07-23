import streamlit as st
from pdf_reader import extract_text
from ai_analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")

st.write("Upload your resume and get AI-powered ATS analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):

        with st.spinner("Reading Resume..."):
            resume = extract_text(uploaded_file)

        with st.spinner("Analyzing with Gemini AI..."):
            result = analyze_resume(resume)

        st.success("Analysis Completed!")

        st.markdown(result)