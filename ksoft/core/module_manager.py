from sqlalchemy.orm import Session
from ksoft.api.models import Module

def add_module(db: Session, name: str, description: str = None):
    """Add a new module to the database"""
    try:
        new_module = Module(name=name, description=description)
        db.add(new_module)
        db.commit()
        db.refresh(new_module)
        return new_module
    except Exception:
        db.rollback()
        # Return existing module if name already exists
        return db.query(Module).filter(Module.name == name).first()

def list_modules(db: Session):
    """Get all modules from the database"""
    return db.query(Module).all()

def delete_module(db: Session, name: str):
    """Delete a module from the database"""
    try:
        module = db.query(Module).filter(Module.name == name).first()
        if module:
            db.delete(module)
            db.commit()
            return True
        return False
    except Exception:
        db.rollback()
        raise
