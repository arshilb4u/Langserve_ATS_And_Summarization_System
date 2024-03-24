import streamlit as st
import os
import PyPDF2 as pdf
import json
import requests


st.title('Applications using Langserve')
st.header('This Application is used to show how you can make a production ready LLM application by using Langserve and Langsmith')
st.sidebar.success('Select any page from below options')
    