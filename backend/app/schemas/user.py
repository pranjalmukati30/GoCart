from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    full_name : str
    email : EmailStr
    password : str


class UserResponse(BaseModel):
    id : int
    full_name : str
    email : EmailStr
    role : str
    created_at : datetime