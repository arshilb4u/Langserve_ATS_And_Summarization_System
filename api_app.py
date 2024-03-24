from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title = "ATS Langchain Server",
    version = "1.0.0",
    description = "API for Application Tracking system using OpenAI LLM"
)

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

model = ChatOpenAI()

Prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
JD Match : In percentage \n
Missing Keyword : In list of words \n
Profile summary : As string

Some additional information Make all the extracted information well formatted with heading in Blod letter and Missing keywords as bullet points
"""

prompt_temp = ChatPromptTemplate.from_template(Prompt)

prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system",'You are a helpful assistant. Please respond to the user request only based on the given context'),
        ("user","Questions : Can you summarize the speech \nContext :{Context}")
    ]
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

add_routes(
    app,
    prompt_temp|model,
    path="/analysis"
)

add_routes(
    app,
    prompt1|model,
    path="/summary"
)

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)