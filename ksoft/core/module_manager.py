from sqlalchemy.orm import Session
from ksoft.api.models import Module

# Function to add a new module
def add_module(db: Session, name: str, description: str = None):
    new_module = Module(name=name, description=description)
    db.add(new_module)
    db.commit()
    db.refresh(new_module)
    return new_module

# Function to list all modules
def list_modules(db: Session):
    return db.query(Module).all()

# Function to get a module by name
def get_module(db: Session, name: str):
    return db.query(Module).filter(Module.name == name).first()

# Function to delete a module
def delete_module(db: Session, name: str):
    module = db.query(Module).filter(Module.name == name).first()
    if module:
        db.delete(module)
        db.commit()
        return True
    return False
