from fastapi import FastAPI

from src.routes import user_route
from starlette.exceptions import HTTPException
from src.util.errors_util import http_error_handler

from src.db.connection import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_route.router)

app.add_exception_handler(HTTPException, http_error_handler)
