
# LangServe ATS and Summarization system with LangSmith

This Application uses Langserve for creating FastApi Endpoints for various services ,So that we can use those services as an API Endpoint for our production Applications . I this i have also used Langsmith as a LLMops service for monitoring the runs.

Below are the services which are deployed as an API:

1) Application Tracking system
2) Document Summarization system





## How to use this Repo

create a virtual environment

you can create virtual env by 3 methods mentioned below

```bash
 virtualenv venv
 python -m venv venv
 conda create -n envname python=x.x anaconda
```
Install requirement.txt
After activiting the Virtual environment

 ```bash
 pip install -r requirements.txt
```

crete a .env file to store API key

```bash
 OPENAI_API_KEY= " " # mention API key here
 LANGCHAIN_API_KEY=" " # Langsmith API key
 LANGCHAIN_PROJECT=" " # Langsmith project name
```

Run server application in a terminal
```bash
 python api_app.py
```
Run client Application in another terminal
```bash
 streamlit streamlit run home.py
```


## Add Routs for different Application in api_app.py  

```python
from langserve import add_routes

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
```


