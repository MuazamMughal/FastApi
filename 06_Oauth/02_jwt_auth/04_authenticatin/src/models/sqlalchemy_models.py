from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy import String, Boolean, UUID, DateTime, Enum

import datetime
import uuid
import enum

class RoleEnum(enum.Enum):
    """
    Enumeration class representing different roles.
    """
    admin = 'admin'
    user = 'user'


class Base(DeclarativeBase):
    pass