from sqlalchemy import Column, Integer, String, Boolean
from app.db.ddbb import Base

class Specialties(Base):
    __tablename__ = "specialties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    descriptions = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
