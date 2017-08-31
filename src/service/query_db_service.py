from src.dao.mongodb_dao import user_profile_dao, user_credential_dao, seq_dao, user_summary_dao, user_education_dao


def query_user_profile(filter):
    doc = user_profile_dao.fetch_single_doc(filter);
    return doc


def insert_user_profile(doc):
    user_profile_dao.insert_single_doc(doc)

def update_user_profile(filter, doc):
    user_profile_dao.update_single_doc(filter, doc)

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


def insert_user_summary(doc):
    user_summary_dao.insert_single_doc(doc)


def query_user_summary(filter):
    doc = user_summary_dao.fetch_single_doc(filter)
    return doc


def update_user_summary(filter, doc):
    doc = user_summary_dao.update_single_doc(filter, doc)


def count_user_summary(filter):
    count = user_summary_dao.count_docs(filter)
    return count


def insert_user_education(doc):
    user_education_dao.insert_single_doc(doc)


def update_user_education(filter, doc):
    user_education_dao.update_single_doc(filter, doc)


def query_user_educations(filter):
    docs = user_education_dao.fetch_batch_docs(filter)
    return docs

def delete_user_education(filter):
    user_education_dao.delete_single_doc(filter)