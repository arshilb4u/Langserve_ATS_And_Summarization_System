
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

## Application View

![Client_LLM_Application](https://github.com/arshilb4u/Langserve_ATS_And_Summarization_System/assets/30823313/4f36953c-e8c8-416b-90e0-a7d7bbba7915)

## FastAPI Endpoints

![Langserve_FastAPI](https://github.com/arshilb4u/Langserve_ATS_And_Summarization_System/assets/30823313/73025ccd-9c4c-4c54-a41f-6ee1ca1c518f)

## Langsmith Dashboard

![Langsmith_ss](https://github.com/arshilb4u/Langserve_ATS_And_Summarization_System/assets/30823313/ca6cd5db-d3cc-4e0e-a7e0-351282b08d56)


## Documentation

[Langserve](https://python.langchain.com/docs/langserve)
[Langsmith](https://python.langchain.com/docs/langsmith/)
