import uuid


def generate_token():
    id = generate_random_uuid()
    token = id.hex
    return token


def generate_random_uuid():
    return uuid.uuid4()
