import json
from flask import Response, g
from datetime import datetime, timedelta
from src.service import query_cache_service

def jsonify(*args, **kwargs):
    headers = {
      "Access-Control-Allow-Origin" : "http://localhost:5000",
      "Access-Control-Allow-Credentials": "true"
    }
    return Response(jsonifyAsText(*args, **kwargs), mimetype='application/json', headers=headers)


def jsonifyAsText(*args, **kwargs):
    return json.dumps(dict(*args, **kwargs))


def successful_ret(**kwargs):
    return jsonify(success=1, code=0, **kwargs)

# failure code (negative)
# -1XX Authentication fail
# -100 token is missing
# -101 token is invalid
# -102 username not found
# -103 username and password not match
# -104 uid not specified

# -2XX Signup fail
# -200 Credential or profile is empty
# -201 Username or password empty
# -202 Username length invalid
# -203 Password length invalid
# -204 Username exist
# -205 Birth date invalid
# -206 Email format invalid
# -207 Phone number format invalid

# -21X Summary fail
# -210 Summary length error

# -22X Education fail
# -220 Education start_t or end_t invalid
# -221 Education start_t is later than end_t 

# -3XX Data invalid
# -300 Email format invalid
# -301 Date invalid
# -302 Phone invalid
# -303 Start_t later than now
# -304 Start_t later than End_t
# -305 End_t later than now

def failure_ret(code=-1, **kwargs):
    return jsonify(success=0, code=code, **kwargs)


def token_ret(token=None, success=1, **kwargs):
    expires = datetime.utcnow() + timedelta(minutes=28)
    resp = jsonify(success=success, **kwargs)
    resp.set_cookie("token", token, expires=expires)
    query_cache_service.renew_token(token)
    return resp
