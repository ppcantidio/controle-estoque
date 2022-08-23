import logging

from ..db.user_db import UserDB
from ..db.product_db import ProductTable
from ..util.log_util import sessao_transacao_log

from starlette.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder


class UserService:
    """
    Class responsible for managing business rules related to users
    """
    def __init__(self, db_session, id_sessao, id_transacao):
        self.sessao_transacao = sessao_transacao_log(id_sessao, id_transacao)
        self.user_db = UserDB(self.sessao_transacao, db_session)

    def create_user(self, user):
        """
        - Verify if exist an user with required email
        - Insert the user at database and return to controller
        """
        user_existence = self.user_db.get_user_by_email(user.email)
        if user_existence:
           raise HTTPException(status_code=400, detail="Email already registered")

        user = jsonable_encoder(user)
        user = self.user_db.create_user(user=user)

        return user

    def get_user(self, user_id: int):
        """
        - Verify if user exist in database and return the result
        to controller
        """
        user = self.user_db.get_user(user_id)

        if user is None:
            raise HTTPException(status_code=404, detail='User not found')

        return user