from asyncio import get_event_loop

from settings import nats_conn_str, topics_listen_to

from utils.nats_controller import NatsController



def main():
    nats_ctrl = NatsController(nats_conn_str, topics_listen_to)
    loop = get_event_loop()
    loop.create_task(nats_ctrl.listen())
    loop.run_forever()


if __name__ == "__main__":
    main()
