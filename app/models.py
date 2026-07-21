from sqlalchemy import TIMESTAMP, Column,String,Integer,Boolean, text

from .database import Base

class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default="True")
    created_at=Column(TIMESTAMP(timezone="True"),nullable=False,server_default=text("now()"))

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    email=Column(String,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone="True"),nullable=False,server_default=text("now()"))