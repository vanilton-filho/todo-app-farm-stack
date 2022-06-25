from typing import Optional
import uuid
from pydantic import BaseModel, Field

class Todo(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    is_done: Optional[bool] = False
