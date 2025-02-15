from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# SQLAlchemy Database Model
class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())

# Pydantic Schema for API Requests/Responses
class ModuleCreate(BaseModel):
    name: str
    description: str = None

class ModuleResponse(ModuleCreate):
    id: int
    created_at: DateTime

    class Config:
        from_attributes = True
