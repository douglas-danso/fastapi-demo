from fastapi import FastAPI
import logging
from contextlib import asynccontextmanager
from .app_config.db_config import startup_db
from .todo_app.todo_controllers import router

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app:FastAPI):
    await startup_db() 
    yield

app = FastAPI(lifespan=lifespan)
@app.get("/")
async def func():
    logger.info(f"request / endpoint!")
    return {"message": "hello world!"}


app.include_router(router)
