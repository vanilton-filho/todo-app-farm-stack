from fastapi import APIRouter
from backend.core.api_settings import api_settings

root_router = APIRouter()

@root_router.get(path="/")
def root():
    return {
        "version": api_settings.API_VERSION, 
        "application_name": api_settings.API_NAME
    }


