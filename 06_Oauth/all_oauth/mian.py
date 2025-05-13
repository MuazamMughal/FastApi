from fastapi import FastAPI , Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime , timedelta
from jose import JWTError , jwt
from passlib.context import CryptContext

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

SECRET_KEY =""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None
    email: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str


#writeing functins to encrypt

pwd_cotnext = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_schema = OAuth2PasswordBearer(tokenUrl="token")

app :FastAPI = FastAPI()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_cotnext.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_cotnext.hash(password)

def get_user(db, username: str) -> UserInDB | None:
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(db, username: str, password: str) -> UserInDB | None:
    user = get_user(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data:dict , expires_date :timedelta | None = None):
    to_encode = data.copy()
    if expires_date:
        expire = datetime.utcnow() + expires_date
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token:str = Depends(oauth_2_schema)):
    creadential_exception = HTTPException( status_code = status.HTTP_401_UNAUTHORIZED,
                                          detail= "could not validate creadentials" , headers= {"WWW-Authenticte" : "Bearer" }):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise creadential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise creadential_exception
    
    
