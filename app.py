from dotenv import load_dotenv
import streamlit as st 
import os
import google.generativeai as genai
import  PyPDF2 as pdf 

load_dotenv()  # load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Gemini Pro Response
 
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text 
def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
     
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
        
    return text


input_prompt="""
Hey act like a skilled or experienced ATS(Application Tracking System)
with a deep understanding of each field, software engineering, data science, data analyst and big data engineer. Your task is to evaluate the resume based on the given job description . You must consider the job market is very competitive and you should provide best assistnce for importving the resumes. Assign the percentage matching based on Job description and the missing keye+words with high accuracy

resume :{text}
description:{jd}

I want the response in one single string having the structure
{{" JD Match : "%", "MissingKerwords:[]", "Profile Summary":""}}

"""

st.title("Smart ATS")
st.text("Improve  Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume", type="pdf",help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        st.write("Pdf Uploaded successfully")
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)
    else:
        st.write("Please upload your resume")
        