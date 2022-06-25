from pydantic import BaseModel

class TodoResponse(BaseModel):
    id: str
    title: str
    description: str
    is_done: bool
    
