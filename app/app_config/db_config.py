import os
from dotenv import load_dotenv
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.todo_app.todo_model import Todos
import logging

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
logger = logging.getLogger(__name__)

async def startup_db():
    logger.info("starting db")
    client = AsyncIOMotorClient(DATABASE_URL)
    # client = AsyncIOMotorClient("mongodb://localhost:27017/Posts_db")
    client.get_default_database()
    await init_beanie(client.get_default_database(), 
    document_models=[Todos]
    )
    logger.info("db started")


async def get_db():
    db = await startup_db()
    try:
        yield db
    finally:
        await db.close()