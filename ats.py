import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gemini_response(input,pdf_content,prompt): 
    model=genai.GenerativeModel("gemini-1.5-pro")
      # Prepare the content correctly
    contents = [input] + pdf_content + [prompt]
    response = model.generate_content(contents)
    return response.text
    #response=model.generate_content([input,pdf_content[0],prompt])
    #return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images=pdf2image.convert_from_bytes(uploaded_file.read()) #converting PDF to Image
        first_page=images[0]
    
        bytearray=io.BytesIO()
        first_page.save(bytearray,format="JPEG")
        bytearray=bytearray.getvalue()

        pdf_parts = [
            {
                'mime_type':'image/jpeg',
                'data':base64.b64encode(bytearray).decode()
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Expert HR Evaluation")

submit2 = st.button("Technical HR Manager Insight")

submit3 = st.button("ATS Scanner Evaluation")

submit4 = st.button("ATS Scanner Skill Highlighting and Resume Rewrite")

# input_prompt1 =''' You are an expert you are an experienced HR with tech experience in the field of any one job role in either data science 
# or web development or big data engineering or data analyst, your task is to review the Provide against the job description
# for all these profiles. Please share your professional evaluation on whether the candidate profile aligns with the role. 
# Highlight the strength and weakness of the applicant in relation to the specified job requirements '''
input_prompt1 = ''' As an HR professional with extensive technical expertise in one of the following roles: Data Scientist, 
Web Developer, Big Data Engineer, or Data Analyst, your task is to conduct a thorough review of the provided candidate profile 
against the job description for the specified role. Assess how well the candidate's experience, skills, and qualifications match 
the role's requirements. Provide a detailed evaluation highlighting both strengths and weaknesses in relation to the job description.'''


# input_prompt2 = ''' You are a technical human resource manager with expertise in field of any one job role in either data science 
# or web development or big data engineering or data analyst, your role is to scrutinize the résumé in light of the job 
# description provided. Share your insights on the candidates' skills for the role from HR perspective. 
# Additionally offer advice on enhancing the candidate skills and identify areas of improvement. '''
input_prompt2 = ''' You are a technical HR manager specializing in one of the following fields: Data Science, Web Development, 
Big Data Engineering, or Data Analysis. Examine the résumé in the context of the provided job description. Offer a detailed 
analysis of the candidate's skills and qualifications from an HR perspective. Provide actionable advice on how the candidate 
can enhance their skills and identify specific areas where improvement is needed to better align with the role.'''

# input_prompt3 = ''' You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding field of any one 
# job role in either data science or web development or big data engineering or data analyst, and deep ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume 
# matches the job description. First the output should come as percentage and then keywords missing in the resume from the job description 
# and last final thoughts. '''
input_prompt3 = ''' As a proficient ATS (Applicant Tracking System) scanner with advanced knowledge in one of the following fields:
Data Science, Web Development, Big Data Engineering, or Data Analysis, evaluate the provided resume against the job description. 
First, calculate and provide the percentage match between the resume and the job description. Next, identify and list the key 
terms and phrases that are present in the job description but missing from the resume. Conclude with an overall assessment of 
how well the resume aligns with the job requirements.'''

# input_prompt4 = ''' You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding field of any one 
# job role in either data science or web development or big data engineering or data analyst, and deep ATS functionality, 
# take my experience as a Business Data Analyst and identify which skills I should highlight if I'm looking to pivot into a role as 
# Business Analyst. You can also try with both your resume and the job description. Additionally, rewrite the resume as you see fit. '''
input_prompt4 = ''' As an expert ATS (Applicant Tracking System) scanner with in-depth understanding of one of the following fields: 
Data Science, Web Development, Big Data Engineering, or Data Analysis, analyze my experience as a Business Data Analyst to 
determine which skills should be emphasized for transitioning into a Business Analyst role. Review both my current resume and the 
Business Analyst job description. Suggest specific skills and experiences to highlight, and provide a revised version of the 
resume to enhance its alignment with the Business Analyst role requirements.'''

if submit1: 
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response=gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("Expert HR Evaluation")
        st.write(response)
    else: 
        st.write("Please upload the resume")
elif submit2:
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response=gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("Technical HR Manager Insight")
        st.write(response)
    else: 
        st.write("Please upload the resume")
elif submit3: 
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response=gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("ATS Scanner Evaluation ")
        st.write(response)
    else: 
        st.write("Please upload the resume")
elif submit4: 
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response=gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else: 
        st.write("ATS Scanner Skill Highlighting and Resume Rewrite")


