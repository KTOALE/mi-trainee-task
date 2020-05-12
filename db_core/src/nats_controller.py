from nats import NATS
from settings import NATS_CONN


class NatsController:

    def __init__(self, topics: list):
        self.nc = NATS()
        self.topics = topics
        self.msg_keeper = {}

    async def handler(self, msg):
        self.msg_keeper[msg.subject] = msg

    async def lets_listen(self):
        await self.nc.connect(NATS_CONN)
        for topic in self.topics:
            await self.nc.subscribe(topic, cb=self.handler)
