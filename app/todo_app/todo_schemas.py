from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class StatusEnum(str,Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"
class TodoSchema(BaseModel):
    title: str
    description: str
    status: StatusEnum = StatusEnum.todo
    timestamp:datetime = datetime.now()

class TodoResponse(TodoSchema):
    pass