import sys
from webthing import (SingleThing, Property, Thing, Value, WebThingServer)
import logging
import tornado.ioloop
from motionsensor import MotionSensor



class MotionSensorThing(Thing):

    # regarding capabilities refer https://iot.mozilla.org/schemas
    # there is also another schema registry http://iotschema.org/docs/full.html not used by webthing

    def __init__(self, description, name, sensor: MotionSensor):
        Thing.__init__(
            self,
            'urn:dev:ops:motionSensor-1',
            'Motion ' + name + ' Sensor',
            ['MotionSensor'],
            description
        )

        self.ioloop = tornado.ioloop.IOLoop.current()
        self.sensor = sensor
        self.sensor.set_listener(self.on_value_changed)

        self.motion = Value(sensor.is_motion)
        self.add_property(
            Property(self,
                     'motion',
                     self.motion,
                     metadata={
                         '@type': 'MotionProperty',
                         'title': 'Motion detected',
                         "type": "boolean",
                         'description': 'Whether ' + name  + ' motion is detected',
                         'readOnly': True,
                     }))

        self.last_motion = Value(sensor.last_motion_date.isoformat())
        self.add_property(
            Property(self,
                     'motion_last_seen',
                     self.last_motion,
                     metadata={
                         'title': 'Motion last seen',
                         "type": "string",
                         'unit': 'datetime',
                         'description': 'The ISO 8601 date time of last movement',
                         'readOnly': True,
                     }))


    def on_value_changed(self):
        self.ioloop.add_callback(self._on_value_changed)

    def _on_value_changed(self):
        self.motion.notify_of_external_update(self.sensor.is_motion)
        self.last_motion.notify_of_external_update(self.sensor.last_motion_date.isoformat())



def run_server(description: str, port: int, name: str, gpio_number:int):
    motion_sensor = MotionSensorThing(description, name, MotionSensor(gpio_number))
    server = WebThingServer(SingleThing(motion_sensor), port=port, disable_host_validation=True)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.info('stopping the server')
        server.stop()
        logging.info('done')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(name)-20s: %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging.getLogger('tornado.access').setLevel(logging.ERROR)
    logging.getLogger('urllib3.connectionpool').setLevel(logging.WARNING)
    run_server("description", int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
