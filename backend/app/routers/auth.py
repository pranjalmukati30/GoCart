from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.security import hash_password



router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse,status_code=201)
def register(user : UserCreate, db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")

    new_user = User(
        full_name = user.full_name,
        email = user.email,
        hashed_password = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user