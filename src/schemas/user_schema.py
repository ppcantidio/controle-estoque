from typing import Union

from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    email: str


class UserCreateSchema(BaseUser):
    password: str
    

class UserOutSchema(BaseUser):
    id: int

    class  Config:
        orm_mode = True
