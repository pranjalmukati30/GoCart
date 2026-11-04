from jose import jwt
from pwdlib import PasswordHash
from app.config import settings
from datetime import datetime, timedelta, timezone


SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
TOKEN_EXP_TIME = 5


def create_access_token(data : dict):
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXP_TIME)
    payload.update({"exp" : expire})

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token

def verify_access_token(token : str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload



password_hash = PasswordHash.recommended()

def hash_password(password : str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password : str, hashed_password : str) -> bool:
    return password_hash.verify(plain_password, hashed_password)