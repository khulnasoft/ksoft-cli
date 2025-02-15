from sqlalchemy.orm import Session
from ksoft.core.bootstrap import SessionLocal
from ksoft.api.models import Module

def get_db():
    """Dependency to get database session"""
    with SessionLocal() as db:
        yield db
