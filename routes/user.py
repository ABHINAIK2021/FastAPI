from fastapi import APIRouter
from config.db import conn
from models.index import UserModel
from schemas.index import UserSchema

UserRouter = APIRouter()

@UserRouter.get("/")
async def select_data():
    return conn.execute(UserModel.select()).fetchall()

@UserRouter.get("/{id}")
async def select_data_by_id(id: int):
    return conn.execute(UserModel.select().where(UserModel.c.id == id)).fetchall()

@UserRouter.post("/")
async def insert_data(user: UserSchema):
    conn.execute(UserModel.insert().values(
        username = user.username,
        password = user.password
    ))
    return conn.execute(UserModel.select()).fetchall()

@UserRouter.put("/{id}")
async def update_data(id: int, user: UserSchema):
    conn.execute(UserModel.update().values(
        username = user.username,
        password = user.password
    ).where(UserModel.c.id == id))
    return conn.execute(UserModel.select()).fetchall()

@UserRouter.delete("/{id}")
async def delete_data(id : int):
    conn.execute(UserModel.delete().where(UserModel.c.id == id))
    return conn.execute(UserModel.select()).fetchall()