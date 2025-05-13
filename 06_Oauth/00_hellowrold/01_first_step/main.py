from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
oauth = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

@app.get("/token" )
def get_verify(token: Annotated[str, Depends( oauth)]):
    return {"token": token}