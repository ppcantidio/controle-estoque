from fastapi import  APIRouter, Request, Depends

from sqlalchemy.orm import Session

from ..schemas.user_schema import UserCreateSchema, UserOutSchema
from ..service.user_service import UserService

from ..util.funcao_util import retorna_sucesso
from ..util.dependences_util import get_db


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/', response_model=UserOutSchema)
async def create_user(user: UserCreateSchema, request: Request, session_db: Session = Depends(get_db)):
    session_id = request.headers.get('session_id')
    transaction_id = request.headers.get('transaction_id')

    user = UserService(session_db, session_id, transaction_id).create_user(user)

    return user


@router.get('/{user_id}', response_model=UserOutSchema)
async def get_user(user_id: int, request: Request, session_db: Session = Depends(get_db)):
    session_id = request.headers.get('session_id')
    transaction_id = request.headers.get('transaction_id')

    user = UserService(session_db, session_id, transaction_id).get_user(user_id)

    return user
