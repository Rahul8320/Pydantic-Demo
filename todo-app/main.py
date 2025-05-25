from http import HTTPStatus
from fastapi import FastAPI

from schemas.api_response import ApiResponse
from routes.todo_routes import todo_router

app = FastAPI()

app.include_router(prefix="/api", router=todo_router)


@app.get("/", status_code=HTTPStatus.OK, tags=["Health"])
def health():
    response = ApiResponse(status=HTTPStatus.OK, message="Api is healthy")
    return response.model_dump(exclude_none=True)
