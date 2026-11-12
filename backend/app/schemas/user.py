from pydantic import BaseModel, EmailStr
from typing import Literal
from datetime import datetime

class UserCreate(BaseModel):
    full_name : str
    email : EmailStr
    password : str


class UserResponse(BaseModel):
    id : int
    full_name : str
    email : EmailStr
    role : Literal["customer", "admin"] = "customer"
    created_at : datetime

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class LoginResponse(BaseModel):
    access_token : str
    token_type : str