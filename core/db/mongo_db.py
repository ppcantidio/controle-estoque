import  os
import logging
import pymongo


class Database:
    def __init__(self, collection, sessao_transacao):
        self.collection = collection
        self.sessao_transacao = sessao_transacao
        self.client = pymongo.MongoClient(os.environ.get("LOCAL_CONNECTION"))
        self.db = self.client.get_database(os.environ.get("DB_NAME"))

    async def insert_one(self, document):
        try:
            logging.info('Inserindo documento no banco de dados', extra=self.sessao_transacao)
            self.collection.insert_one(document)
            logging.info('Documento inserido no banco de dados', extra=self.sessao_transacao)
        except:
            logging.error('Erro ao inserir documento no banco de dados', extra=self.sessao_transacao)


    async def select_one(self, where):
        try:
            logging.info('Realizando pesquisa no banco de dados')
            document = self.collection.find_one(where)
            logging.info('Pesquisa no banco de dados finalizada', extra=self.sessao_transacao)
            return document
        except:
            logging.error('Erro ao realizar pesquisa no banco de dados', extra=self.sessao_transacao)