from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import databse
from resources.routers import api_router
from contextlib import asynccontextmanager


origins = ["http://localhost", "http://localhost:4200"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await databse.connect()
    yield
    await databse.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=True,
    allow_crediential=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
