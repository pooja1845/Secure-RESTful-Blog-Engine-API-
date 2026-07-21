from typing import Optional ,List
from warnings import deprecated
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor #ka use query results ko dictionary format me receive karne ke liye hota hai.
import time
from .database import engine
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas,utils,models
from .routers import post,user,auth


models.Base.metadata.create_all(bind=engine)

app=FastAPI() # app is an instance of FastAPI


""""
# -------------through postgrsql -------------------------

while True:
    try:
        conn = psycopg2.connect(host='localhost',database='postgres',user='postgres',
                                password='12345',cursor_factory=RealDictCursor)
        cur = conn.cursor()
        print("Database is successfully connected...")
        break
    except Exception as error:
        print("Failed to connect")
        print("error :", error)
        time.sleep(2)



# my_posts=[{"title":"places to visit","content":"raj,kol,delhi","id":1},
#          {"title":"places to eat","content":"kota,jaipur","id":2}]


def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return  p

def find_index_posts(id):
    for i,p in enumerate(my_posts):
        if p["id"]==id:
            return i

@app.get("/")
async def root(response:Response):
    return{"message":"welcome to my api !!!"}

@app.get("/posts")
def get_posts():
    cur.execute('''SELECT * FROM posts ;''')
    posts=cur.fetchall()
    conn.commit()
    # print(posts)
    return{"data":posts}

@app.get("/posts/{id}")
def get_post(id:int,response:Response):
    cur.execute('''SELECT * FROM posts WHERE id=%s''',(str(id),))
    post=cur.fetchone()
    conn.commit()
    # post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id {id} is not found")
    
    return{"detail":post}

# @app.post("/create")
# def addpost(payload: dict=Body(...)):
#     return{"message":"successfully create the post",
#            "New Message":f"title : {payload["title"]}  content: {payload["content"]}"}

@app.post("/posts")
def create_post(post:Post):
    cur.execute('''INSERT INTO posts(title,content,published) VALUES(%s,%s,%s) RETURNING * '''
                ,(post.title,post.content,post.published))
    post_new=cur.fetchone()
    conn.commit()
    return{"data":post_new}
    # post_dict=post.model_dump()
    # post_dict["id"]=randrange(1,10000)
    # my_posts.append(post_dict)
    # return{"message":post}

@app.put("/posts/{id}")
def update_post(id:int,post:Post):

    cur.execute(''' UPDATE posts SET title=%s ,content=%s ,published=%s WHERE id=%s RETURNING *''',
                (post.title,post.content,post.published,(str(id),)))
    updt_post=cur.fetchone()
    conn.commit()
    
    if updt_post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} is not exist")
    
    return{"data":updt_post}
    # index=find_index_posts(id)
    # if index==None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id {id} is not found")
    # dict_post=post.model_dump()
    # dict_post["id"]=id
    # my_posts[index]=dict_post
    # return{"message":f"Successfully update id :{id}","detail":dict_post}

@app.delete("/posts/{id}")
def remove_post(id:int):

    cur.execute(''' DELETE FROM posts WHERE id=%s RETURNING *''',(str(id),))
    del_post=cur.fetchone()
    if del_post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id {id} is not found")
    conn.commit()
    return{"deleted post":del_post}
    # index=find_index_posts(id)
    # if index==None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id {id} is not found")
    # my_posts.pop(index)
    # return{"message":f"Successfully deleted post with entry id : {id}"}

"""

#? ORM (Object Relational Mapping) allows you to interact with the database using 
#? Python classes and objects instead of writing raw SQL queries.

#instead of manually defining the tables in postgres we can define our tables as python models
#Queries will be made through python ,no need for sql
# SQLAlchemy is the most popular ORM library in Python. It lets you work with 
# databases using Python objects instead of writing raw SQL queries.

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def show():
    return {"message":"welcome"}