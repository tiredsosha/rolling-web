from aiohttp import web


class Handler:
    def __init__(self, mqtt):
        self.mqtt = mqtt

    async def ping(self, request):
        return web.Response(text="pong")

    async def command(self, request):
        command = str(await request.text()).split('=')[1]
        await self.mqtt.publish('table/command', command)
        return web.Response(text=f"table's going {command}")

    async def scenario(self, request):
        scenario = str(await request.text()).split('=')[1]
        await self.mqtt.publish('table/scenario', scenario)
        return web.Response(text=f"starting {scenario} in 10 second")

    async def index(self, request):
        with open('configs/index.html', encoding="utf8") as html:
            html = html.read()
        return web.Response(text=html, content_type='text/html')