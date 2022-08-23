from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .connection import Base


class ProductTable(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
