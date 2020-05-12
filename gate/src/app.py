from aiohttp import web
from buisness_handlers import gen_secret, get_secret
from system_handlers import login, logout, create_user

def conf_server_params():
    app = web.Application()

    HOST = "localhost"
    PORT = "7777"

    app.add_routes(
        [
            web.post("/login", login),
            web.post("/logout", logout),
            web.post("/create_user", create_user),
            web.post("/generate", gen_secret),
            web.get("/secrets/{secret_key}", get_secret),
        ]
    )
    return {
        "app":app,
        "host":HOST,
        "port":PORT,
    }



def launch_app():
    server_params = conf_server_params()
    web.run_app(**server_params)

if __name__=="__main__":
    launch_app()