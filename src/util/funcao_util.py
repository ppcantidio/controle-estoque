import bcrypt
import string
import random


def retorna_sucesso(documento, recurso):
    retorno = {
        'status': 'sucesso',
        'dados': documento,
        'recurso': recurso
    }

    return retorno


def criptografa_senha(senha):
    salt = bcrypt.gensalt(8)
    hashed = bcrypt.hashpw(senha, salt)
    return hashed


def gerar_chave(size=64, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))