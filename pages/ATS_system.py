import streamlit as st
import os
import PyPDF2 as pdf
import json
import requests

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


st.title("This is ATS system")
st.subheader("This is an ATS system using OpenAI LLM to check if your resume is appropriate with Job description also this ATS service is accessed \
             as a API which is created by using Langserve")
st.sidebar.success("You have selected ATS system")

jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        url = 'http://localhost:8000/analysis/invoke'
        response = requests.post(
            url,
            json = {
                'input':{
                    'text': text,
                    'jd': jd
                }
            }
        )
        st.subheader(response.json()['output']['content'])

