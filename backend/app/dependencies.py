from app.database import SessionLocal


# for get_current_user dependency
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.models.user import User
from app.security import verify_access_token
from jose import JWTError, ExpiredSignatureError


def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()



# for get_current_user dependency
security = HTTPBearer()

def get_current_user(auth_info:HTTPAuthorizationCredentials = Depends(security), db:Session = Depends(get_db)):
    token = auth_info.credentials

    try:
        payload = verify_access_token(token)
        user_id = payload.get("sub")

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")

    user = db.query(User).filter(User.id == int(user_id)).first()
    
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user

def admin_required(user:User = Depends(get_current_user)):
    if user.role == "admin":
        return user
    else:
        raise HTTPException(status_code=403, detail="Admin Acess Only")