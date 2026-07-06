from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime
from app.database import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)
    simplified_output = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)