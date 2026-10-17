
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5175",
        "http://127.0.0.1:5175",
    ],
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
