from nats import NATS


class NatsController:

    def __init__(self, conn_str):
        self.nc = NATS()
        self.conn_str = conn_str
        # self.topics = topics
        self.msg_keeper = {}

    async def listen(self, topics_and_handlers:iter):
        await self.nc.connect(self.conn_str)
        for topic, handler in topics_and_handlers:
            await self.nc.subscribe(topic, cb=handler)
        # await self.nc.close()

    async def publish(self, topic, payload=None):
        await self.nc.connect(self.conn_str)
        await self.nc.publish(topic, payload=payload)
        await self.nc.close()

    async def request(self, topic, payload=None):
        await self.nc.connect(self.conn_str)
        response = await self.nc.request(topic, payload=payload)
        return response
