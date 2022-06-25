from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.api_router import api_router
from backend.api.root_router import root_router
from backend.core.api_settings import api_settings

app = FastAPI(title=api_settings.API_NAME)

origins = [api_settings.REACT_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(root_router, tags=["root"])
app.include_router(api_router, prefix=api_settings.API_V1_PATH)
