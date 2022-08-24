from ..util.log_util import sessao_transacao_log
from ..db.product_db import ProductDB

class ProductService:
    def __init__(self, session_db, session_id, transaction_id):
        self.sessao_transacao = sessao_transacao_log(session_id, transaction_id)
        self.product_db = ProductDB(self.sessao_transacao, session_db)

    def create_product(self, product: object):
        product = self.product_db = self.product_db.create_product(product)

        return product
