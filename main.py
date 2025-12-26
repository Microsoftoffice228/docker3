from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()

@app.get("/")
def get_random_number():
    return {"numberss": random.randint(1, 100)}

