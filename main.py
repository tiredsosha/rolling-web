import yaml

from aiohttp import web

from server.routes import Handler
from mqtt.run import Mqtt
from mqtt.entities import Mqtt_conf


def main():
    with open('configs/mqtt.yaml') as mqtt:
        mqtt_conf = Mqtt_conf(**yaml.safe_load(mqtt))

    app = web.Application()
    mqtt = Mqtt(mqtt_conf.host, mqtt_conf.port, mqtt_conf.username,
                mqtt_conf.password)

    handler = Handler(mqtt)

    app.add_routes([
        web.get('/', handler.index),
        web.get('/ping', handler.ping),
        web.post('/command', handler.command),
        web.post('/scenario', handler.scenario)
    ])

    web.run_app(app)


if __name__ == '__main__':
    main()
