async def handler(self, msg):
    self.msg_keeper[msg.subject] = msg