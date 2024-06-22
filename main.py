from fastapi import FastAPI

from db import databse
from resources.routers import api_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    await databse.connect()
    yield
    await databse.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

