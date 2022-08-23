from fastapi import  APIRouter, Request, Depends

from sqlalchemy.orm import Session

from ..schemas.user_schema import UserCreateSchema
from ..service.user_service import UserService

from ..util.funcao_util import retorna_sucesso
from ..util.dependences_util import get_db


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/')
async def create_user(user: UserCreateSchema, request: Request, db_session: Session = Depends(get_db)):
    id_sessao = request.headers.get('id_sessao')
    id_transacao = request.headers.get('id_transacao')

    user = UserService(db_session, id_sessao, id_transacao).create_user(user)

    return retorna_sucesso(user, 'user')


@router.get('/{user_id}')
async def get_user(user_id: int, request: Request, db_session: Session = Depends(get_db)):
    id_sessao = request.headers.get('id_sessao')
    id_transacao = request.headers.get('id_transacao')

    user = UserService(db_session, id_sessao, id_transacao).get_user(user_id)

    return retorna_sucesso(user, 'user')
