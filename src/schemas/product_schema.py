from typing import Union

from pydantic import BaseModel


class BaseProduct(BaseModel):
    name: str
    quantity: int
    price: int
    category: str
    description: Union[str, None] = None


class ProductCreateSchema(BaseProduct):
    pass


class ProductOutSchema(BaseProduct):
    id: int
    user_id: int

    class  Config:
        orm_mode = True