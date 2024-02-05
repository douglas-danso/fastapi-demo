from fastapi import APIRouter,Request
from . import todo_services
from .todo_model import Todos
from .todo_schemas import TodoSchema
import logging

router = APIRouter()

logger=logging.getLogger(__name__)

@router.post("/todo")
async def create_todo(data: TodoSchema):
    
    return await todo_services.create_todos_service(data)
    

@router.get("/todo")
async def get_todo():
    return await todo_services.get_todos_service()
    


@router.put("/todo/{todo_id}")
async def edit_todo(todo_id, data:TodoSchema):
    return await todo_services.edit_todos_service(todo_id,data)
    
       

@router.delete("/todo/{todo_id}")
async def delete_todo(todo_id):
    return await todo_services.delete_todos_service(todo_id)
   