from fastapi import Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union, Any, Optional
from uuid import UUID
import secrets
import string

from ..models.auth import  TokenData, User, RegisterUser, UserOutput
from ..utils.db_dep import get_db
from ..utils.helpers import InvalidUserException, verify_password, ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES
from ..data.auth import db_signup_users, get_user, get_user_by_id, get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(db, username: str, password: str):
    try:
        user = get_user(db, username)
    except InvalidUserException:
        return False

    if not verify_password(password, user.hashed_password):
        return False
    return user



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if not isinstance(SECRET_KEY, str):
        raise ValueError("SECRET_KEY must be a string")

    if not isinstance(ALGORITHM, str):
            raise ValueError("ALGORITHM must be a string")
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()

    if not isinstance(SECRET_KEY, str):
        raise ValueError("SECRET_KEY must be a string")

    if not isinstance(ALGORITHM, str):
            raise ValueError("ALGORITHM must be a string")
    
    # Convert UUID to string if it's present in the data
    if 'id' in to_encode and isinstance(to_encode['id'], UUID):
        to_encode['id'] = str(to_encode['id'])

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=7)  # Set the expiration time for refresh tokens to 7 days

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

