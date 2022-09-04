from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from ..schemas.product_schema import ProductCreateSchema

from .connection import Base


class ProductTable(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))


class ProductDB:
    def __init__(self, sessao_transacao: dict, db: Session):
        self.db = db
        self.session_transaction= sessao_transacao

    def get_product(self, product_id: int):
        self.db.query(ProductTable).filter(ProductTable.id == product_id).first()

    def create_product(self, product: ProductCreateSchema, user_id: int):
        product_db = ProductTable(**product.dict(), user_id=user_id)
        self.db.add(product_db)
        self.db.commit()
        self.db.refresh(product_db)
        return product_db
