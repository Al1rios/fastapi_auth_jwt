from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

auth_routes = APIRouter()

class User(BaseModel):
    username: str,
    email: EmailStr


@auth_routes.post("/login")
def login(user: User):
    print(user)
    return "success"