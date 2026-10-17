
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def greeting():
    return "Welcome to FastAPI....."

@app.get("/users")
def get_users():
    return {
        "name": "Srikanth",
        "age": 22,
        "phone": 6305784358
    }
