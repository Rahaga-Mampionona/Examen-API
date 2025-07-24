from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Mampionona"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/square/{number}")
async def square_number(number: int):
    return {"number": number, "square": number ** 2}

@app.get("/greet")
async def greet_user(name: Optional[str] = Query(default="stranger", description="Nom de l'utilisateur")):
    return {"greeting": f"Welcome, {name}!"}

@app.get("/sum")
async def sum_numbers(a: int = 0, b: int = 0):
    return {"a": a, "b": b, "sum": a + b}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

@app.post("/echo")
async def echo_data(data: dict):
    return {"received": data}
