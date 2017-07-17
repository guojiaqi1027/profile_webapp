from dao.mongodb_dao import user_profile_dao, user_credential_dao


def query_user_profile(uid):
    filter = {'uid': uid};
    doc = user_profile_dao.fetch_single_doc(filter);
    return doc


def query_user_credential(uid):
    filter = {'uid': uid};
    doc = user_credential_dao.fetch_single_doc(filter);
    return doc
