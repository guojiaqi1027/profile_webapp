var SETTINGS  = {
  DOMAIN: '//localhost:9000'
};

var CONSTANTS = {
  AUTH_SIGNUP_URL: SETTINGS.DOMAIN + '/public_api/signup',
  LOGIN_URL: SETTINGS.DOMAIN + '/public_api/authentication',
  GET_PROFILE_URL: SETTINGS.DOMAIN + '/profile_api/get_profile',
  UPDATE_PROFILE_URL: SETTINGS.DOMAIN + '/profile_api/update_profile',
  GET_SUMMARY_URL: SETTINGS.DOMAIN + '/summary_api/get_summary',
  UPDATE_SUMMARY_URL: SETTINGS.DOMAIN + '/summary_api/update_summary',
  ADD_EDUCATION_URL: SETTINGS.DOMAIN + '/education_api/insert_education',
  GET_EDUCATIONS_URL: SETTINGS.DOMAIN + '/education_api/get_educations',
  DELETE_EDUCATION_URL: SETTINGS.DOMAIN + '/education_api/delete_education',
  UPDATE_EDUCATION_URL: SETTINGS.DOMAIN + '/education_api/update_education'
}
module.exports = CONSTANTS;