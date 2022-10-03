from fastapi import FastAPI, APIRouter, HTTPException, Depends, status
import mysql.connector
import models, schema, utils
from database import engine
from routers import post, user, vote
from config import settings
from fastapi.middleware.cors import CORSMiddleware


#models.Base.metadata.create_all(bind=engine)


origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




#conn = mysql.connector.connect(user= 'root', password='root',
                                   #host='localhost', database='fastapi')
#cursor = conn.cursor()




app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World!!!"}











