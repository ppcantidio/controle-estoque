

def sessao_transacao_log(id_sessao, id_transacao, collection=None):
    log = {
        'id_sessao': id_sessao,
        'id_transacao': id_transacao
    }

    if collection is not None:
        log['collection'] = collection
        
    return log
