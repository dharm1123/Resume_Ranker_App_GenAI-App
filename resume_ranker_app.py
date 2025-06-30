import streamlit as st
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables from .env
load_dotenv()

# Configure Azure OpenAI model
llm = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_type="azure",
    temperature=0.7,
    top_p=0.9,
    max_tokens=1000,
 )

# Function to extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Function to get LLM score
def get_resume_score(jd_text, resume_text):
    prompt = f"""
You are an expert HR evaluator.

Job Description:
{jd_text}

Candidate Resume:
{resume_text}

Give a score from 0 to 100 based on how well the resume matches the job description.
Only return the number.
"""
    response = llm([HumanMessage(content=prompt)])
    try:
        score = int(''.join(filter(str.isdigit, response.content.strip())))
    except:
        score = 0
    return score

# Streamlit UI
st.title("Resume Ranker ")
st.write("Upload a Job Description and up to 10 Resumes in PDF format.")

jd_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")
resume_files = st.file_uploader("Upload Resumes (PDF)", type="pdf", accept_multiple_files=True)

if jd_file and resume_files:
    jd_text = extract_text_from_pdf(jd_file)
    
    ranking = []
    
    with st.spinner("Ranking resumes..."):
        for resume in resume_files:
            resume_text = extract_text_from_pdf(resume)
            score = get_resume_score(jd_text, resume_text)
            ranking.append((resume.name, score))

    # Sort by score descending
    ranking.sort(key=lambda x: x[1], reverse=True)

    st.subheader(" Ranked Resumes:")
    for i, (name, score) in enumerate(ranking, start=1):
        st.write(f"**{i}. {name}** - Score: {score}")
