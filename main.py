from fastapi import FastAPI, Query, status
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

students_db = []

#@app.get("/")
#async def root():
#  return {"message": "Hello world"}

#@app.get("/hello/{name}")
#async def say_hello(name: str):
#   return {"message": f"Hello {name}"}

@app.get("/")
async def root():
  return {"message": "Welcome Mampionona"}

@app.get("/welcome", status_code=200)
async def welcome_user(name: str = Query(..., description="Mampionona")):
    return {"message": f"Welcome {name}"}


class Student(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int








