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

st.title("Get the Document summary")
st.subheader("This is document summarization system which will help to summarize document and this system also uses Langserve to getit as a API response")
st.sidebar.success("You have selected Document summarization")
uploaded_file=st.file_uploader("Upload the document for summariation",type="pdf",help="Please uplaod the pdf")

submit = st.button("summary")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        url = 'http://localhost:8000/summary/invoke'
        response = requests.post(
        url,
        json = {
            'input':{
                'Context': text
                
            }
        }
        )
    st.write(response.json()['output']['content'])

