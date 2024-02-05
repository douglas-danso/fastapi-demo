from beanie import Document
from .todo_schemas import TodoSchema
class Todos(Document,TodoSchema):
    class Settings:
        collection = "todos"
    class Config:
        from_attributes = True

