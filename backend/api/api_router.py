from fastapi import APIRouter
from backend.api.v1.routers import (
    todo_router,
)

api_router = APIRouter()
api_router.include_router(todo_router.router, prefix="/todo", tags=["todo"])

