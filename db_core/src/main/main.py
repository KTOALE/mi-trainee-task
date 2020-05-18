from asyncio import get_event_loop
from settings import nats_conn_str, topics_listen_to
from utils.coro_tasks import set_secret, get_secret
from utils.mongo_tools import init_mongo
from utils.nats_controller import NatsController

def main():
    init_mongo()
    nats_ctrl = NatsController(nats_conn_str)
    secrets = set_secret, get_secret,
    loop = get_event_loop()
    loop.create_task(
        nats_ctrl.listen(
            zip(topics_listen_to, secrets)
        )
    )
    loop.run_forever()


if __name__ == "__main__":
    main()
