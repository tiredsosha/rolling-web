import mqttools


class Mqtt:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = int(port)
        self.username = username
        self.password = password.encode('UTF-8')

    async def publish(self, topic, message):
        async with mqttools.Client(
                self.host,
                self.port,
                'fiona',
                username=self.username,
                password=self.password,
        ) as client:
            client.publish(mqttools.Message(topic, message.encode('UTF-8')))
