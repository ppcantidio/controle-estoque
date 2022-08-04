import logging

from core.util import strings
from core.db.mongo_db import Database
from core.util.log_util import sessao_transacao_log

from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


class ProdutoService:
    """
    Classe responsável por gerenciar as regras
    de negocio relaciondas a produtos
    """
    def __init__(self, nm_id_sessao, nm_id_transacao):
        self.sessao_transacao = sessao_transacao_log(nm_id_sessao, nm_id_transacao)

    async def criar_produto(self, produto: dict):
        await self.__verifica_existencia_produto(produto)
        await Database(self.sessao_transacao).insert_one(produto)

    async def __verifica_existencia_produto(self, produto):
        existencia = await Database(self.sessao_transacao).select_one({'cdReferencia': produto.get('cdReferencia')})
        if existencia is not None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=strings.UNABLE_TO_FOLLOW_YOURSELF,
            )
