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

@app.get("/welcome/{name}")
def welcome_user(name: str):
    return {"message":f"Welcome {name}"}


Array_students =[]

class Students(BaseModel):
    Reference:str
    FirstName:str
    LastName:str
    Age:int
@app.post("/students",response_model=list[Students],status_code=201)
def create_students(new_student:Students):
    Array_students.append(new_student)
    return Array_students




@app.get("/studens}")
def get_students_List_objet( ):
    return {"total":len(Array_students)}

@app.put("/students")






# uvicorn main:app --reload

