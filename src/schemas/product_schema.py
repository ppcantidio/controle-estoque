from typing import Union

from pydantic import BaseModel


class BaseProduct(BaseModel):
    nome: str
    quantidade: int
    preco: int
    categoria: str
    descricao: Union[str, None] = None


class ProductCreateSchema(BaseProduct):
    pass


class ProductSchema(BaseProduct):
    id: int
    usuario_id: int

    class  Config:
        orm_mode = True