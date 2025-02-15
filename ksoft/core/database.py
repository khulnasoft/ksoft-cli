from sqlalchemy.orm import Session
from ksoft.core.bootstrap import SessionLocal

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example function to add a new module
def add_module(db: Session, name: str, description: str = None):
    from ksoft.api.models import Module
    new_module = Module(name=name, description=description)
    db.add(new_module)
    db.commit()
    db.refresh(new_module)
    return new_module
