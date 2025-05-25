from typing import List, Optional

from models.todo_entity import TodoEntity

# In-memory storage for todos
todos: List[TodoEntity] = []


class TodoRepository:
    """
    A repository class for managing Todo items in an in-memory list.
    Provides methods to create, retrieve, update, and delete todos.
    """

    def create_todo(self, todo: TodoEntity) -> None:
        """
        Adds a new todo to the in-memory list.

        Args:
            todo (TodoEntity): The todo item to be added.
        """
        todos.append(todo)

    def get_todo(self, todo_id: int) -> Optional[TodoEntity]:
        """
        Retrieves a todo by its ID.

        Args:
            todo_id (int): The ID of the todo to retrieve.

        Returns:
            Optional[TodoEntity]: The todo item if found, otherwise None.
        """
        for todo in todos:
            if todo.id == todo_id:
                return todo

        return None

    def get_all_todos(self) -> List[TodoEntity]:
        """
        Retrieves all todos in the in-memory list.

        Returns:
            List[TodoEntity]: A list of all todo items.
        """
        return todos

    def update_todo(
        self, todo_id: int, updated_todo: TodoEntity
    ) -> Optional[TodoEntity]:
        """
        Updates an existing todo with new data.

        Args:
            todo_id (int): The ID of the todo to update.
            updated_todo (TodoEntity): The updated todo item.

        Returns:
            Optional[TodoEntity]: The updated todo item if found and updated, otherwise None.
        """
        for index, todo in enumerate(todos):
            if todo.id == todo_id:
                todos[index] = updated_todo.model_copy(update={"id": todo_id})
                return todos[index]

        return None

    def delete_todo(self, todo_id: int) -> Optional[bool]:
        """
        Deletes a todo by its ID.

        Args:
            todo_id (int): The ID of the todo to delete.

        Returns:
            Optional[bool]: True if found and deleted, otherwise None.
        """
        for index, todo in enumerate(todos):
            if todo.id == todo_id:
                todos.pop(index)
                return True

        return None
