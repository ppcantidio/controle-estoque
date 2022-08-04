from fastapi import FastAPI

from api.routes import produto
from starlette.exceptions import HTTPException
from api.errors.http_error import http_error_handler

app = FastAPI()

app.include_router(produto.router)

app.add_exception_handler(HTTPException, http_error_handler)