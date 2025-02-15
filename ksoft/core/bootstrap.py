from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ksoft.api.models import Base

# Database connection URL
DATABASE_URL = "sqlite:///./ksoft.db"

# Create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database tables."""
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")
