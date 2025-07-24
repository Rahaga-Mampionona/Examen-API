from fastapi import FastAPI, Query, status
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()



@app.get("/")
async def root():
  return {"message": "Hello world"}

@app.get("/hello/{name}")
async def say_hello(name: str):
   return {"message": f"Hello {name}"}

@app.get("/")
async def root():
  return {"message": "Welcome Mampionona"}

@app.get("/welcome", status_code=200)
async def welcome_user(name: str = Query(..., description="Mampionona")):
    return {"message": f"Welcome {name}"}


students_db = []

class Student(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int





@app.post("/students", status_code=status.HTTP_201_CREATED)
async def add_students(students : List[Student] = [    {"Reference": "STD24092", "FirstName": "Mampionona", "LastName": "Rahaga", "Age": 20},
    {"Reference": "STD24042", "FirstName": "Haja", "LastName": "Jean", "Age": 18}
]): 
    
    for student in students_db:
        students_db.append(student)
    return students_db

@app.get("/students", status_code=200)
async def get_students():
    return students_db

@app.put("/students", status_code=200)
async def upsert_student(student: Student):
    for idx, existing_student in enumerate(students_db):
        if existing_student.Reference == student.Reference:
            students_db[idx] = student
            return {"message": "Student updated", "student": student}
    students_db.append(student)
    return {"message": "Student added", "student": student}




