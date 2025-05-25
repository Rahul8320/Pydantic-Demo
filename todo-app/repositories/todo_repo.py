from typing import List, Optional

from models.todo_entity import TodoEntity

# In-memory storage for todos
todos: List[TodoEntity] = []


class TodoRepository:
    def create_todo(self, todo: TodoEntity) -> None:
        todos.append(todo)

    def get_todo(self, todo_id: int) -> Optional[TodoEntity]:
        for todo in todos:
            if todo.id == todo_id:
                return todo

        return None

    def get_all_todos(self) -> List[TodoEntity]:
        return todos
