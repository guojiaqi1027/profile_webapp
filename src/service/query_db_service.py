from src.dao.mongodb_dao import user_profile_dao, user_credential_dao, seq_dao


def query_user_profile(filter):
    doc = user_profile_dao.fetch_single_doc(filter);
    return doc


def insert_user_profile(doc):
    user_profile_dao.insert_single_doc(doc)


def query_user_credential(filter):
    doc = user_credential_dao.fetch_single_doc(filter);
    return doc


def insert_user_credential(doc):
    user_credential_dao.insert_single_doc(doc)
    return


def get_sequence(seq_id):
    filter = { 'id': seq_id }
    seq = seq_dao.fetch_single_doc(filter).get('seq', 0)
    seq = int(seq)
    return seq


def increment_sequence(seq_id):
    filter = { 'id': seq_id }
    seq = seq_dao.fetch_single_doc(filter)
    if seq:
        seq['seq'] = seq.get('seq', 0) + 1
        seq_dao.update_single_doc(filter, seq)
    else:
        seq = {
            'id': seq_id,
            'seq': 1
        }
        seq_dao.insert_single_doc(seq)
    return seq['seq']


def vending_id(seq_id):
    id = get_sequence(seq_id) + 1
    id = increment_sequence(seq_id)
    return id