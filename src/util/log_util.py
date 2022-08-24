

def sessao_transacao_log(session_id, transaction_id, collection=None):
    log = {
        'session_id': session_id,
        'transaction_id': transaction_id
    }

    if collection is not None:
        log['collection'] = collection
        
    return log
