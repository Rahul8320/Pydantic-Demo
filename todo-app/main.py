from http import HTTPStatus
from fastapi import FastAPI
from schemas.api_response import ApiResponse

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=ApiResponse)
def health():
    response = ApiResponse(status=HTTPStatus.OK, message="Api is healthy")
    return response.model_dump(exclude_none=True)
