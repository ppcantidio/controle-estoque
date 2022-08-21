from fastapi import HTTPException

from ..db.database import Database
from ..db.redis_db import RedisDB


async def create_id_sessao(usuario: dict):
    return str(usuario.get('_id'))


async def auth_user(email: str, senha: str, sessao_transacao: dict):
    usuario = await Database('usuario', sessao_transacao).select_one({'email': email, 'senha': senha})
    if usuario is None:
        raise HTTPException()

    id_sessao = await create_id_sessao(usuario)
    id_usuario = str(usuario.get('_id'))

    RedisDB(sessao_transacao).insert_value(
        key=id_sessao,
        value=id_usuario
    )

    return id_sessao


async def verify_session(sessao_transacao):
    id_usuario = RedisDB(sessao_transacao).get_by_key(sessao_transacao.get('id_sessao'))
    if id_usuario is None:
        raise HTTPException()

    return id_usuario


async def logout(sessao_transcao):
    RedisDB(sessao_transcao).delete_by_key(sessao_transcao.get('id_sessao'))
