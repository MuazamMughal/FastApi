from datetime import timedelta
from typing import Annotated, Optional

from fastapi import Depends, FastAPI, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm

from models import Token, User
from data import fake_users_db

from service import authenticate_user, create_access_token, create_refresh_token ,get_current_active_user, tokens_service, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES
