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
def failure_ret(code=-1, **kwargs):
    return jsonify(success=0, code=code, **kwargs)
