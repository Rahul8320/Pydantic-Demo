from pydantic import BaseModel, Field


class TodoEntity(BaseModel):
    id: int
    task: str = Field(..., max_length=250)
    completed: bool = False
