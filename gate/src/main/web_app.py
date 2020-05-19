from aiohttp import web
from handlers.buisness import gen_secret, get_secret
from handlers.system import login, logout, create_user, index
from settings import SERVER_HOST, SERVER_PORT


def conf_server_params():
    app = web.Application()

    app.add_routes(
        [
            web.post("/", index),
            web.post("/login", login),
            web.post("/logout", logout),
            web.post("/create_user", create_user),
            web.post("/generate", gen_secret),
            web.get("/secrets/{secret_key}", get_secret),
        ]
    )
    return {
        "app": app,
        "host": SERVER_HOST,
        "port": SERVER_PORT,
    }


def launch_app():
    server_params = conf_server_params()
    web.run_app(**server_params)


if __name__ == "__main__":
    launch_app()
