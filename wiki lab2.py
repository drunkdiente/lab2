from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()


@app.get("/{title}")
def titles(title: str):
    return wikipedia.search(title)


@app.get("/multi/{title}")
def titles_count(title: str,number_of_titles = int):
    return wikipedia.search(title, results=number_of_titles)


class Request(BaseModel):
    title: str
    output: str


class Request_Input(BaseModel):
    title: str


@app.post("/",response_model=Request)
def create_list_of_titles(request_input: Request_Input):
    return Request(title=request_input.title, output=wikipedia.search(request_input.title, results=1)[0])








