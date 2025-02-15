import pytest 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ksoft.api.models import Base

@pytest.fixture(scope="function")
def test_db():
    """Test database fixture"""
    engine = create_engine("sqlite:///./test.db")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)