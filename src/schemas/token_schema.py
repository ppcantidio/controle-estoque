from typing import Union
from lib2to3.pytree import Base
from pydantic import BaseModel


class Token(BaseModel):
    acess_token = str
    token_type = str


class TokenData(BaseModel):
    username: Union[str, None] = None
