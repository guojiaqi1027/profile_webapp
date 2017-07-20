import json
from flask import Response, g


def jsonify(*args, **kwargs):
    return Response(jsonifyAsText(*args, **kwargs), mimetype='application/json')


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

def failure_ret(code=-1, **kwargs):
    return jsonify(success=0, code=code, **kwargs)
