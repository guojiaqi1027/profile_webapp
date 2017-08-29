var SETTINGS  = {
  DOMAIN: '//localhost:9000'
};

var CONSTANTS = {
  AUTH_SIGNUP_URL: SETTINGS.DOMAIN + '/public_api/signup',
  LOGIN_URL: SETTINGS.DOMAIN + '/public_api/authentication',
  GET_PROFILE_URL: SETTINGS.DOMAIN + '/public_api/get_user_profile'
}
module.exports = CONSTANTS;