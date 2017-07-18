from dao.mongodb_dao import user_profile_dao, user_credential_dao


def query_user_profile(filter):
    doc = user_profile_dao.fetch_single_doc(filter);
    return doc


def query_user_credential(filter):
    doc = user_credential_dao.fetch_single_doc(filter);
    return doc
