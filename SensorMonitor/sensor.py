__author__ = 'James Myatt'

import SensorMonitor


class Factory:
    def __init__(self):
        self.__dict = {
            'w1therm': SensorMonitor.w1therm.Factory
            }
   
    def create(self, spec):
        factory = self.__dict[spec['type']]()
        return factory.create(spec)


class SensorFactory:
    def __init__(self, sensor_cls, factory_if):
        self.sensor_cls = sensor_cls
        self.factory_if = factory_if
    
    def create(self, spec=None):
        sensor_if = self.factory_if.create(spec)
        return self.sensor_cls(sensor_if)


class Sensor:
    def __init__(self, sensor_if):
        self.sensor_if = sensor_if

    def get_measurement(self):
        return self.sensor_if.read_data()


class SensorInterface:
    def __init__(self):
        pass

    def read_data(self):
        return None
