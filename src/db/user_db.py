from sqlalchemy.orm import Session, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from ..schemas.user_schema import UserCreateSchema, UserOutSchema

from .connection import Base


class UserTable(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    products = relationship("ProductTable")


class UserDB:
    def __init__(self, sessao_transacao, db: Session):
        self.db = db
        self.sessao_transacao = sessao_transacao

    def get_user_auth(self, user_email):
        db_user = self.db.query(UserTable).filter(UserTable.email == user_email).first()
        return db_user

    def get_user(self, user_id: int):
        db_user = self.db.query(UserTable).filter(UserTable.id == user_id).first()
        return UserOutSchema.from_orm(db_user) 

    def get_user_by_email(self, user_email: str):
        return self.db.query(UserTable).filter(UserTable.email == user_email).first()

    def create_user(self, user: UserCreateSchema):
        db_user = UserTable(**user)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserOutSchema.from_orm(db_user)
