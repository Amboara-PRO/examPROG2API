from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenue sur FastAPI"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Bonjour {name} !"}

class User(BaseModel):
    name: str
    age: int

@app.post("/users/")
def create_user(user: User):
    return {
        "message": f"Utilisateur {user.name} créé",
        "age": user.age
    }
