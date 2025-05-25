from http import HTTPStatus
from typing import List
from fastapi import APIRouter, Depends, HTTPException

from schemas.api_response import ApiResponse
from schemas.todo import TodoDto, CreateTodo
from models.todo_entity import TodoEntity
from repositories.todo_repo import TodoRepository

todo_router = APIRouter(prefix="/todos", tags=["Todos"])

next_id: int = 1


# get todo repository
def get_todo_repository() -> TodoRepository:
    return TodoRepository()


# Create new todo
@todo_router.post("/", status_code=HTTPStatus.CREATED, response_model=ApiResponse)
def create_todo(
    request: CreateTodo, todo_repo: TodoRepository = Depends(get_todo_repository)
):
    global next_id
    todo = TodoEntity(id=next_id, task=request.task, completed=request.completed)
    todo_repo.create_todo(todo)
    next_id += 1

    return ApiResponse(
        status=HTTPStatus.CREATED,
        message="Todo created successfully",
        data=todo,
    )


# Get all todos
@todo_router.get("/", status_code=HTTPStatus.OK, response_model=ApiResponse)
def get_all_routes(todo_repo: TodoRepository = Depends(get_todo_repository)):
    todos: List[TodoDto] = [
        TodoDto.from_entity(todo=todo) for todo in todo_repo.get_all_todos()
    ]

    return ApiResponse(
        status=HTTPStatus.OK, message="Todos fetched successfully", data=todos
    )


# Get todo by id
@todo_router.get("/{id}", status_code=HTTPStatus.OK, response_model=ApiResponse)
def get_todo(id: int, todo_repo: TodoRepository = Depends(get_todo_repository)):
    todo = todo_repo.get_todo(id)

    if todo is not None:
        return ApiResponse(
            status=HTTPStatus.OK,
            message="Todo fetched successfully",
            data=TodoDto.from_entity(todo=todo),
        )

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail=f"Todo with id: {id} not found in our database",
    )
