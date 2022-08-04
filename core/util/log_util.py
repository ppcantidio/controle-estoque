

def sessao_transacao_log(nm_id_sessao, nm_id_transacao, collection=None):
    log = {
        'nm_id_sessao': nm_id_sessao,
        'nm_id_transacao': nm_id_transacao
    }

    if collection is not None:
        log['collection'] = collection
        
    return log
