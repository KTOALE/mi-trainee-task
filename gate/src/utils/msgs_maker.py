from json import dumps


def make_secret_msg(login, secret, secret_key, encrypt=False):
    payload = dumps(
        {
            "secret": secret,
            "secret_key": secret_key,
            "login": login,
        }
    )
    return payload.encode() if encrypt else payload
