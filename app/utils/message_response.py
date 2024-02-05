from fastapi import status
from enum import Enum
from fastapi.responses import JSONResponse

class ActionsEnum(str,Enum):
    deleted = "deleted"
    created = "created"
    updated = "updated"

async def success_message(action:ActionsEnum):
    return {
        "details":f"todo task {action} successfully",
        "status": status.HTTP_200_OK
    }

async def success_message_data(data):
    return {
        "details":"todo tasks retrieved successfully",
        "data":data,
        "status": status.HTTP_200_OK
    }


async def error_message(message:str, status:status):
    return {
        "error": message,
        "status": status
    }

