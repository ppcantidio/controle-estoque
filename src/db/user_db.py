from sqlalchemy.orm import Session

from ..models.user_model import UserTable
from ..schemas.user_schema import UserCreateSchema


class UserDB:
    def __init__(self, sessao_transacao, db: Session):
        self.db = db
        self.sessao_transacao = sessao_transacao

    def get_user(self, user_id: int):
        return self.db.query(UserTable).filter(UserTable.id == user_id).first()

    def get_user_by_email(self, user_email: str):
        return self.db.query(UserTable).filter(UserTable.id == user_email).first()

    def create_user(self, user: UserCreateSchema):
        db_user = UserTable(user)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
