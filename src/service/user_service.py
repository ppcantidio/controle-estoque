import logging
import bcrypt

from ..util import strings
from ..db.user_db import UserDB
from ..db.redis_db import RedisDB
from ..util.log_util import sessao_transacao_log
from ..util.funcao_util import criptografa_senha, gerar_chave, retorna_sucesso

from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


class UserService:
    """
    Classe responsável por gerenciar as regras
    de negocio relaciondas a usuarios
    """
    def __init__(self, db_session, id_sessao, id_transacao):
        self.sessao_transacao = sessao_transacao_log(id_sessao, id_transacao)
        self.user_db = UserDB(self.sessao_transacao, db_session)

    async def criar_usuario(self, user):
        existencia_usuario = await self.user_db.get_user_by_email(user.email)
        if existencia_usuario:
           raise HTTPException(status_code=400, detail="Já existe um usuario cadastrado com esse email")

        user = self.user_db.create_user(user=user)

        return user
