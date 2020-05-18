from nats import NATS


class NatsController:

    def __init__(self, conn_str):
        self.nc = NATS()
        self.conn_str = conn_str
        self.msg_keeper = {}


    async def publish(self, topic, payload=None):
        await self.nc.connect(self.conn_str)
        await self.nc.publish(topic, payload=payload)
        await self.nc.close()

    async def request(self, topic, payload=None):
        await self.nc.connect(self.conn_str)
        response = await self.nc.request(topic, payload=payload)
        return response
