from conexion import db
from fastapi import FastAPI
from models import User

users = db.collection(u'users')

app = FastAPI()

@app.get("/")
async def root():
    usersRef = users.get()

    for user in usersRef:
        print(f'{user.id} => {user.to_dict()}')
    return 

@app.post("/addUser")
async def addUser(user: User):
    userAdd = users.document(f'{user.id}')
    userAdd.set({
        u'first': user.name,
        u'last': user.lastName,
        u'born': user.born
    })
    return 

