from fastapi import FastAPI, HTTPException
from h11._abnf import status_code
from pydantic import BaseModel, Field
from typing import List
from datetime import time
import json

from starlette import status

app = FastAPI()


@app.get("/hello")
def root():
    return ({"message": "Hello word"})


class WelcomeRequest(BaseModel):
    name:str

@app.get("/welcome")
def welcome_user(request: WelcomeRequest):
    return {f"Bienvenue {request.name}"}


class Students:
    Reference:str
    FirstName:str
    LastName:str
    Age:int
@app.post("/students")



@app.get("/studens}")
def get_students_List_objet(request: Students ):
    return (Students)






# uvicorn main:app --reload

