from pydantic import BaseModel
from typing import Optional

class SchemaSpecialties(BaseModel):
    id: Optional[int] = None
    name: str
    descriptions: Optional[str] = None
    is_active: bool = True

class SchemaSpecialtiesCreate(BaseModel):
    name: str
    descriptions: Optional[str] = None
    is_active: bool = True

class SchemaSpecialtiesUpdate(BaseModel):
    ''''
    Schema for update specialties
    '''
    name : Optional [str] = None
    descriptions: Optional [str] = None
    is_active : Optional [bool] = None