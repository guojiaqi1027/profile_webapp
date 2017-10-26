from src.service import query_db_service
from src.configs import SEARCH_PRIORITY_CONFIG
from src.action.profile import profile_action
from src.action.summary import summary_action
from src.action.education import education_action
from src.action.experience import experience_action

def get_all_uids():
    return query_db_service.get_sequence('uid')

def search_all_uids(keys, uid):
    resp = [];
    for x in xrange(1, uid+1):
        item = search_uid(keys, x)
        if item:
            resp.append(item)
    return resp


def search_uid(keys, uid):
    profile = profile_action.get_profile_by_uid_action(uid)
    educations = education_action.get_educations_by_uid(uid)
    summary = summary_action.get_sumamry_by_uid_action(uid)
    experiences = experience_action.get_experiences_by_uid(uid)
    max_prior = 0
    for key in keys:
        prior = max(search_profile(key, profile), search_summary(key, summary), search_educations(key, educations), search_experiences(key, experiences))
        # return None if 1 key not match
        if prior <= 0:
            return None
        max_prior = max(max_prior, prior)
    item = {
        'profile': profile,
        'priority': max_prior
    }
    return item


def search_profile(key, profile):
    name = profile.get('name', '').lower()
    title = profile.get('title', '').lower()
    company = profile.get('company', '').lower()
    address = profile.get('address', '').lower()
    if name.find(key) >= 0 or title.find(key) >= 0 or company.find(key) >= 0 or address.find(key) >= 0:
        return SEARCH_PRIORITY_CONFIG.PROFILE_PRIORITY
    else:
        return -1


def search_summary(key, summary):
    summary = (summary or "").lower()
    if summary.find(key) >= 0:
        return SEARCH_PRIORITY_CONFIG.SUMMARY_PRIORITY
    else:
        return -1


def search_educations(key, educations):
    for x in xrange(len(educations)):
        school = educations[x].get('school', '').lower()
        major = educations[x].get('major', '').lower()
        degree = educations[x].get('degree', '').lower()
        if school.find(key) >= 0 or major.find(key) >= 0 or degree.find(key) >= 0:
            return SEARCH_PRIORITY_CONFIG.EDUCATION_PRIORITY
    else:
        return -1


def search_experiences(key, experiences):
    for x in xrange(len(experiences)):
        company = experiences[x].get('company', '').lower()
        title = experiences[x].get('title', '').lower()
        desc = experiences[x].get('desc', '').lower()
        if company.find(key) >= 0 or title.find(key) >= 0 or desc.find(key) >= 0:
            return SEARCH_PRIORITY_CONFIG.EXPERIENCE_PRIORITY
    else:
        return -1
