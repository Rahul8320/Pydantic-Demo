from http import HTTPStatus
from typing import List
from fastapi import APIRouter, HTTPException

from schemas.api_response import ApiResponse
from schemas.todo import TodoDto, CreateTodo
from models.todo_entity import TodoEntity

todo_router = APIRouter(prefix="/todos", tags=["Todos"])

todos: List[TodoEntity] = []
next_id: int = 1


# Create new todo
@todo_router.post("/", status_code=HTTPStatus.CREATED)
def create_todo(request: CreateTodo):
    global next_id
    newTodo = TodoEntity(id=next_id, task=request.task, completed=request.completed)
    todos.append(newTodo)
    next_id += 1
    response = ApiResponse(
        status=HTTPStatus.CREATED,
        message="Todo created successfully",
        data=newTodo,
    )
    return response.model_dump(exclude_none=True)


# Get all todos
@todo_router.get("/", status_code=HTTPStatus.OK)
def get_all_routes():
    myTodos: List[TodoDto] = [TodoDto.from_entity(todo=todo) for todo in todos]
    response = ApiResponse(
        status=HTTPStatus.OK, message="Todos fetched successfully", data=myTodos
    )
    return response.model_dump(exclude_none=True)


# Get todo by id
@todo_router.get("/{id}", status_code=HTTPStatus.OK)
def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            response = ApiResponse(
                status=HTTPStatus.OK,
                message="Todo fetched successfully",
                data=TodoDto.from_entity(todo=todo),
            )
            return response.model_dump(exclude_none=True)

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail=f"Todo with id: {id} not found in our database",
    )
