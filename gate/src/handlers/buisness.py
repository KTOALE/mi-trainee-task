from aiohttp.web_request import Request
from aiohttp.web import Response

from settings import nats_conn_str
from utils.nats_controller import NatsController

from utils.msgs_maker import make_secret_msg


async def gen_secret(request: Request):
    resp_params = {}
    nats_ctrl = NatsController(nats_conn_str)
    try:
        print(f"request_type: {type(request)}")
        print(f"url: {request.url}")
        req = await request.json()
        email = req.get("email")
        secret_phrase = req.get("secret_phrase")
        secret = req.get("secret")
        payload = make_secret_msg(
            email, secret, secret_phrase,
            make_bytes=True,
        )
        await nats_ctrl.publish("db_core.set", payload=payload)
        resp_params["text"] = "OK"
        resp_params["status"] = 200
    except Exception as e:
        print(f"Error happens!!! {e}")
        resp_params.update({
            "status": 500,
            "text": "Server Internal Error",
        })
    return Response(**resp_params)


async def get_secret(request):
    pass
