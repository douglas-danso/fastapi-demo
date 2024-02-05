from beanie import PydanticObjectId
from .todo_model import Todos
from .todo_schemas import TodoSchema
from fastapi import status
from app.utils import message_response as response
import logging


logger = logging.getLogger(__name__)
async def create_todos_service(data: TodoSchema):
    logger.info("starting service")
    try:
        todo_data = data.model_dump()
        todos = Todos(**todo_data)
        await todos.insert()
        return await response.success_message("created")
    
    except Exception as e:
        logger.error(e)
        return await response.error_message(
                "Internal server error", 
                status.HTTP_500_INTERNAL_SERVER_ERROR)

async def edit_todos_service(todo_id: PydanticObjectId , data: TodoSchema):
    try:
        existing_todo = await Todos.get(todo_id)
        if existing_todo:
            todo_data = data.model_dump()
            update_data = {"$set": todo_data}
            await existing_todo.update(update_data)
            return await response.success_message("updated")
        else:
            return await response.error_message(
                "todo task not found", 
                status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(e)
        return await response.error_message(
                "Internal server error", 
                status.HTTP_500_INTERNAL_SERVER_ERROR)
    
async def delete_todos_service(todo_id: PydanticObjectId ):
    try:
        existing_todo = await Todos.get(todo_id)
        if existing_todo:
            await existing_todo.delete()
            return await response.success_message("deleted")
        else:
            return await response.error_message(
                "todo task not found", 
                status.HTTP_404_NOT_FOUND)
        
    except Exception as e:
        logger.error(e)
        return await response.error_message(
                "Internal server error", 
                status.HTTP_500_INTERNAL_SERVER_ERROR)


async def get_todos_service():
    try:
        existing_todo = await Todos.find_all().to_list()
        logger.info(existing_todo)
        if existing_todo:
            return await response.success_message_data(existing_todo)
        else:
            return await response.error_message(
                "todo task not found", 
                status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(e)
        return await response.error_message(
                "Internal server error", 
                status.HTTP_500_INTERNAL_SERVER_ERROR)