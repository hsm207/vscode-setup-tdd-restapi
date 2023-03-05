from typing import List
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/sum")
def sum(x: List[int]) -> int:
    """
    Sums a list of integers
    """
    total = 0
    for i in x:
        total += i

    return total


def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
