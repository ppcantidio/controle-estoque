import os
import redis


class RedisDB:
    def __init__(self, sessao_transcao):
        self.sessao_transacao = sessao_transcao
        self.client = redis.Redis(
            host=os.environ.get('REDIS_HOST'),
            port=os.environ.get('REDIS_PORT')
        )

    def get_by_key(self, key):
        self.client.get(key)
    
    def delete_by_key(self, key):
        self.client.delete(key)

    def insert_value(self, key, value):
        self.client.delete(key, value)
