from typing import List
from fastapi import APIRouter, HTTPException, status
from backend.api.v1.responses.todo_response import TodoResponse
from backend.domain.models.todo_model import Todo
from fastapi.responses import Response
from backend.api.v1.serializers.todo_serializer import (
    todo_serializer,
    todo_list_serializer
)
from backend.domain.services.todo_service import (
    fetch_all,
    fetch_by_id,
    create,
    update,
    update_status,
    remove,
)

router = APIRouter()    

@router.get(path="/",  response_model=List[TodoResponse])
async def get_todo():
    """Obtém todos as tarefas."""
    response = await fetch_all()
    return todo_list_serializer(response)

@router.get(path="/{id}", response_model=TodoResponse,)
async def get_todo_by_id(id: str):
    """Obtém uma tarefa por id."""
    response = await fetch_by_id(id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Not found TODO of id {id}")
    return todo_serializer(response)
    

@router.post(path="/", response_model=TodoResponse, status_code=201)
async def post_todo(todo: Todo):
    """Cria um nova tarefa com título e descrição."""
    result = await create(todo.dict())
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Something wrong happened")

    return todo_serializer(result)
    

@router.put("/{id}", response_model=TodoResponse)
async def put_todo(id: str, todo: Todo):
    """Atualiza uma tarefa por id com título e descrição."""
    document = await fetch_by_id(id)
    if document is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found TODO of id {id}")
    
    response = await update(id, todo.dict())
    if not response:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Not found TODO of id {id} or something wrong happened")
    return todo_serializer(response)
    
 
@router.put("/{id}/done", status_code=204)
async def put_status(id: str):    
    """Marca se uma tarefa foi concluída ou não"""
    response = await update_status(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found TODO of id {id}")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
  
@router.delete("/{id}", status_code=204,)
async def delete_todo(id: str):
    """Remove uma tarefa por id."""
    response = await remove(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found TODO of id {id}")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
