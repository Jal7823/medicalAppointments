from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.db.ddbb import get_db
from app.models.modelSpecialties import Specialties as modelSpecialty
from app.schemas.schemaSpecialties import SchemaSpecialties as SpecialtiesSchema,SchemaSpecialtiesCreate,SchemaSpecialtiesUpdate

router = APIRouter()

@router.get('/specialties/', response_model=list[SpecialtiesSchema], status_code=status.HTTP_200_OK)
def get_specialties(db: Session = Depends(get_db)):
    data = db.query(modelSpecialty).filter(modelSpecialty.is_active == True).all()
    if not data:
        raise HTTPException(status_code=404, detail='Item not found')
    return data

@router.post('/specialties/', response_model=SpecialtiesSchema, status_code=status.HTTP_201_CREATED)
def createSpecialties(new_data: SchemaSpecialtiesCreate, db: Session = Depends(get_db)):
    new_item = modelSpecialty(**new_data.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get('/specialties/{id}',response_model=SpecialtiesSchema,status_code=status.HTTP_200_OK)
def get_specialty(id:int,db:Session = Depends(get_db)):
    item = db.query(modelSpecialty).filter(modelSpecialty.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item

@router.put('/specialties/{id}', response_model=SpecialtiesSchema, status_code=status.HTTP_200_OK)
def put_specialty(id: int, new_data: SchemaSpecialtiesCreate, db: Session = Depends(get_db)):
    item = db.query(modelSpecialty).filter(modelSpecialty.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')

    # Aquí actualizas los campos con los nuevos valores
    item.name = new_data.name
    item.descriptions = new_data.descriptions
    item.is_active = new_data.is_active

    db.commit()
    db.refresh(item)
    return item

@router.patch('/specialties/{id}', response_model=SpecialtiesSchema, status_code=status.HTTP_200_OK)
def patch_specialty(id: int, new_data: SchemaSpecialtiesUpdate, db: Session = Depends(get_db)):
    item = db.query(modelSpecialty).filter(modelSpecialty.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')

    if new_data.name is not None:
        item.name = new_data.name
    if new_data.descriptions is not None:
        item.descriptions = new_data.descriptions
    if new_data.is_active is not None:
        item.is_active = new_data.is_active

    db.commit()
    db.refresh(item)
    return item

@router.delete('/specialties/{id}', status_code=status.HTTP_200_OK)
def delete_specialty(id: int, db: Session = Depends(get_db)):
    item = db.query(modelSpecialty).filter(modelSpecialty.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.is_active = False
    db.commit()
    db.refresh(item)
    return {"message": "Item deleted successfully"}
