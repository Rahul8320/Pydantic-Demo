from typing import Optional
from pydantic import BaseModel, Field

from models.todo_entity import TodoEntity


class CreateTodo(BaseModel):
    task: str = Field(..., max_length=250)
    completed: bool = Field(default=False)


class UpdateTodo(BaseModel):
    task: Optional[str] = Field(..., max_length=250)
    completed: Optional[bool] = Field(default=False)


class TodoDto(BaseModel):
    id: int
    task: str
    completed: bool

    @classmethod
    def from_entity(cls, todo: TodoEntity) -> "TodoDto":
        return cls(id=todo.id, task=todo.task, completed=todo.completed)

    @classmethod
    def to_entity(cls) -> TodoEntity:
        return TodoEntity(id=cls.id, task=cls.task, completed=cls.completed)
