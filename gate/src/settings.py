from os import environ

NATS_HOST = environ.get("NATS_HOST", "localhost")
NATS_PORT = environ.get("NATS_PORT", "4222")
topics_listen_to = environ.get("TOPICS_TO_LISTEN", "db_coro.set,db_coro.get".split(","))
nats_conn_str = f"nats://{NATS_HOST}:{int(NATS_PORT)}"

