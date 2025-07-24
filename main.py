from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
