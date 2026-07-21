from ..database import get_db
from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from .. import schemas,models,oauth2
from fastapi import FastAPI,Response,status,HTTPException
from typing import List

router=APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=List[schemas.Post])
def getposts(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts

@router.post("/",response_model=schemas.Post)
def create_post(post:schemas.PostCreate,db: Session = Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
    new_post=models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/{id}",response_model=schemas.Post)
def get_post_byId(id:int,db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} is not found")
    return post

@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db: Session = Depends(get_db)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if not post:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} is not exist")
    post_query.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()
    return post_query.first()

@router.delete("/{id}")
def delete_post(id:int,db: Session = Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if not post:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} is not exist")
    post_query.delete(synchronize_session=False)
    db.commit()
    return{"message":f"Successfully deleted post with id :{id}"}

