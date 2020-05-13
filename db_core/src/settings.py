from utils.nats_controller import NatsController

nats_conn_str = "nats://nats_server:8888"
topics_listen_to = None
nats_ctrl = NatsController(nats_conn_str, topics_listen_to)