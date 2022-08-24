from fastapi import APIRouter, Request, Depends

from sqlalchemy.orm import Session

from ..schemas.product_schema import ProductCreateSchema, ProductOutSchema
from ..service.product_service import ProductService
from ..util.dependences_util import get_db


router = APIRouter(
    prefix='/product',
    tags=['product']
)


@router.post('/', response_model=ProductOutSchema)
def create_product(product: ProductCreateSchema, request: Request, session_db: Session = Depends(get_db)):
    session_id = request.headers.get('session_id')
    transaction_id = request.headers.get('transaction_id')

    product = ProductService(session_id, transaction_id, session_db).create_product(product)

    return product

