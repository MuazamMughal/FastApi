from pydantic import BaseModel, EmailStr
from uuid import UUID
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str

class TokenData(BaseModel):
    username: str | None = None
    id: UUID | None = None
    
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"