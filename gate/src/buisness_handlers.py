from aiohttp.web_request import Request


async def gen_secret(request: Request):
    try:
        print(f"request_type: {type(request)}")
        print(f"url: {request.url}")
    except:
        print("ERROR!!!")


async def get_secret(request):
    pass
