from fastapi import FastAPI , Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from pydantic import BaseModel


#first i have to make fake database



app :FastAPI = FastAPI()
