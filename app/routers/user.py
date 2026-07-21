from ..database import get_db
from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from .. import schemas,models,utils
from fastapi import FastAPI,Response,status,HTTPException
from typing import List

router=APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/",response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):
    
    hashed_password=utils.hash(user.password)
    user.password=hashed_password    

    new_user=models.User(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/",response_model=List[schemas.UserOut])
def getUsers(db: Session = Depends(get_db)):
    users=db.query(models.User).all()
    return users

@router.get("/{id}",response_model=schemas.UserOut)
def get_user_byId(id:int,db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id :{id} is not found")
    return user