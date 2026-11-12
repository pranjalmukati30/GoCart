from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserResponse, UserLogin, LoginResponse
from app.dependencies import get_db, get_current_user
from sqlalchemy.orm import Session
from app.models.user import User
from app.security import hash_password, verify_password, create_access_token



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

@router.post("/login", response_model=LoginResponse)
def login(login_data : UserLogin, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()

    if user:
        verify = verify_password(login_data.password, user.hashed_password)
        if verify:
            data = {
                "sub" : str(user.id),
                "role" : user.role
            }
            token = create_access_token(data)
            return{
                "access_token" : token,
                "token_type" : "bearer"
            }
        else:
            raise HTTPException(status_code=401, detail="Invalid Credentials")

    else:
        raise HTTPException(status_code=401, detail="Invalid Credentials")


@router.get("/me", response_model=UserResponse)
def me(user:User = Depends(get_current_user)):
    return user