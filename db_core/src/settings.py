from os import environ

MONGO_HOST = environ.get("MONGO_HOST", "localhost")
MONGO_PORT = environ.get("MONGO_PORT", "27017")
NATS_HOST = environ.get("NATS_HOST", "localhost")
NATS_PORT = environ.get("NATS_PORT", "4222")


nats_conn_str = f"nats://{NATS_HOST}:{NATS_PORT}"
topics_listen_to = environ.get("TOPICS_TO_LISTEN", "db_coro.set,db_coro.get".split(","))
mongo_conn = {
    "host": MONGO_HOST,
    "port": int(MONGO_PORT),
}
