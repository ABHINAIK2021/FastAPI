from fastapi import FastAPI
from routes.index import UserRouter

app = FastAPI()

app.include_router(UserRouter)