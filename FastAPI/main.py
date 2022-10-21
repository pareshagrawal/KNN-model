from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI,HTTPException
from models import User,Gender,Role,UserUpdateRequest

app = FastAPI()

db : List[User] = [
    User(
        id = UUID("0394796e-fe19-4202-ae29-73821e73fce2"),
        firstName = "Yush",
        lastName = "Mittal",
        gender = Gender.male,
        role = [Role.admin]
    ),
    User(
        id = UUID("70ab6487-d5da-46d2-a8a3-d7ab779304d6"),
        firstName = "Paresh",
        lastName = "Agrawal",
        gender = Gender.male,
        role = [Role.student,Role.admin]
    )
]

@app.get("/")
async def root():
    return {"hello" : "world"}

@app.get("/api/v1/users")
async def fetchUser():
    return db
    
@app.post("/api/v1/users")
async def addUser(user : User):
    db.append(user)

@app.delete("/api/v1/users/{user_id}")
async def deleteUser(user_id : UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f'user with {user_id} does not exist'
    )

@app.put("/api/v1/users/{user_id}")
async def UpdateUser(userUpdate : UserUpdateRequest,user_id : UUID):
    for user in db:
        if user.id == user_id:
            if userUpdate.firstName is not None:
                user.firstName = userUpdate.firstName
            if userUpdate.lastName is not None:
                user.lastName = userUpdate.lastName
            if userUpdate.middleName is not None:
                user.middleName = userUpdate.middleName
            if userUpdate.role is not None:
                user.role = userUpdate.role
            return
    raise HTTPException(
        status_code = 404,
        detail = f'user with {user_id} does not exist'
    )
