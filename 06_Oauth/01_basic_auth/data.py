from pydantic import BaseModel
from typing import Optional


class UserDict(BaseModel):
    username: str
    email: str
    full_name: str
    hashed_password: str
    disabled: Optional[bool]



fake_users_db  = {
    "johndoe":{
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "jondo@gmail.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice":{
        "username": "alice",
        "full_name": "Alice",
        "email": "",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    
    }
    
 }
