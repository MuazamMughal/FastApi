from sqlalchemy.orm import Session
from typing import Union
from uuid import UUID

from ..models.sqlalchemy_models import USER
from ..models.auth import  RegisterUser
from ..utils.helpers import get_password_hash, InvalidUserException

async def db_signup_users(
    user_data: RegisterUser, db: Session
):
    # Check if user already exists
    existing_user = db.query(USER).filter((USER.username == user_data.username) | (USER.email == user_data.email)).first()
    if existing_user:
        raise InvalidUserException(status_code=400, detail="Email or username already registered")

    # Hash the password
    hashed_password = get_password_hash(user_data.password)

    # Create new user instance
    new_user = USER(
        username=user_data.username,
        email=user_data.email,
        full_name=user_data.full_name,
        hashed_password=hashed_password,
    )

    # Add new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return the new user data
    return new_user