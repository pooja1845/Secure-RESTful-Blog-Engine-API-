from fastapi import APIRouter,Depends,Response,status,HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import database,schemas,models,utils,oauth2
router=APIRouter(
    tags=["Authorization"]
)

@router.post("/login",response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(database.get_db)):
   user= db.query(models.User).filter(models.User.email==user_credentials.username).first()
   #with OAuth2PasswordRequestForm i have to use username field for email OR we can do with another manner also

   if not user:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
   
   if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
   
   access_token=oauth2.create_access_token(data={"user_id":user.id})
   return{"access_token":access_token,"token_type":"bearer"}

    
