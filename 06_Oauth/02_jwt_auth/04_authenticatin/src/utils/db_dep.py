from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import OperationalError

import time
import os
from dotenv import load_dotenv, find_dotenv

_: bool = load_dotenv(find_dotenv())

DB_URL = os.environ.get("DB_URL")

if DB_URL is None:
    raise Exception("No DB_URL environment variable found")

# Enable connection pooling with pessimistic testing
engine = create_engine(DB_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
