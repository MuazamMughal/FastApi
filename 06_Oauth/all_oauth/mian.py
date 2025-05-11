from fastapi import FastAPI , Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from pydantic import BaseModel


#first i have to make fake database
db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johando@gmail.com",
        "hashed_password": "$2b$12$KIX3v0x1Q4Z5J6g7Y8e5Oe9j1qz5f5F5F5F5F5F5F5F5F5F5F5F",
        "disabled": False,
    }
}




app :FastAPI = FastAPI()
