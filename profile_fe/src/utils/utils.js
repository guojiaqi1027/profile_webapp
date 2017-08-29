import Cookies from 'js.cookie';
class UTILS {
  static setCookie(key, value) {
    if (!key || !value) {
      return;
    }
    var now = new Date();
    var expires_time = now.getTime() + 1800 * 1000;
    var expires = new Date();
    expires.setTime(expires_time);
    Cookies.set(key, value, { 'expires': expires.toGMTString() });
  }
};
export default UTILS;