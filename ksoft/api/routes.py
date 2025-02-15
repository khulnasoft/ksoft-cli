from fastapi import APIRouter
from ksoft.core.database import SessionLocal, Module
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def root():
    return {"message": "Welcome to KSoft API"}

@router.get("/modules")
async def list_modules(db: Session = next(get_db())):
    """Get all registered modules"""
    modules = db.query(Module).all()
    return {"modules": [module.name for module in modules]}
