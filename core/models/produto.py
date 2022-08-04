from typing import Union

from pydantic import BaseModel


class ProdutoCriar(BaseModel):
    nmNome: str
    nrQuantidade: int
    vlPreco: int
    nmCategoria: str
    nmDescricao: Union[str, None] = None
