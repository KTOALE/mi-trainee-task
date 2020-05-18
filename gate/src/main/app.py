from aiohttp import web
from handlers.buisness import gen_secret, get_secret
from handlers.system import login, logout, create_user

def conf_server_params():
    app = web.Application()

    HOST = "127.0.0.1"
    PORT = 9999

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