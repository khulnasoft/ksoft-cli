from sqlalchemy.orm import Session
from ksoft.core.bootstrap import SessionLocal

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
