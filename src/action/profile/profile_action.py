from src.service import query_db_service


def get_profile_by_uid_action(uid):
  if not uid:
    return None

  filter = {
    'uid': uid
  }
  doc = query_db_service.query_user_profile(filter)
  return doc
