from asyncio import get_event_loop
from settings import nats_conn_str, topics_listen_to
from utils.coro_tasks import set_secret, get_secret
from utils.mongo_tools import init_mongo
from utils.nats_controller import NatsController

def main():
    try:
        print("Init Mongo")
        init_mongo()
        print("Init Mongo complete")

        print("Start to launch nats subscribing coro tasks...")
        nats_ctrl = NatsController(nats_conn_str)
        secrets = set_secret, get_secret,
        loop = get_event_loop()
        loop.create_task(
            nats_ctrl.listen(
                zip(topics_listen_to, secrets)
            )
        )
        print("Launch loop")
        loop.run_forever()
    except Exception as e:
        print(f"ERROROORORORORORORORORORO!!!!! ::: {e}")


if __name__ == "__main__":
    main()
