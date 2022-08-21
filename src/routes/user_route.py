from fastapi import  APIRouter, Request, Depends

from sqlalchemy.orm import Session

from ..schemas.user_schema import UserCreateSchema
from ..service.user_service import UserService

from ..util.funcao_util import retorna_sucesso

from ..db.connection import SessionLocal, engine

router = APIRouter(
    prefix='/usuario',
    tags=['usuario']
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/')
async def registrar_usuario(usuario: UserCreateSchema, request: Request, db_session: Session = Depends(get_db)):
    id_sessao = request.headers.get('id_sessao')
    id_transacao = request.headers.get('id_transacao')

    usuario = await UserService(db_session, id_sessao, id_transacao).criar_usuario(usuario)

    return retorna_sucesso(usuario, 'usuario')