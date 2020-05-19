from os import environ

NATS_HOST = environ.get("NATS_HOST", "localhost")
NATS_PORT = environ.get("NATS_PORT", "4222")
topics_listen_to = environ.get("TOPICS_TO_LISTEN", "db_core.set,db_core.get".split(","))
nats_conn_str = f"nats://{NATS_HOST}:{int(NATS_PORT)}"

SERVER_HOST = environ.get("SERVER_HOST","0.0.0.0")
SERVER_PORT = environ.get("SERVER_PORT",9999)
