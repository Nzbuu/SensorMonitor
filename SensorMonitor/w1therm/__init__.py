__author__ = 'James Myatt'
__version__ = '0.0.1'

__all__ = ['interface']

from ..sensor import Sensor
import interface


class Factory:
    def __init__(self, factory=None):
        if not factory:
            factory = interface.Factory()
        self.__factory = factory

    def create(self, sensor_id=None):
        sensor_if, sensor_id = self.__factory.create(sensor_id)
        return W1Therm(sensor_id, sensor_if)


class W1Therm(Sensor):
    def __init__(self, sensor_id, sensor_if):
        Sensor.__init__(self)
        self.sensor_id = sensor_id
        self.interface = sensor_if

    def read_data(self):
        return self.interface.read_data()

    def get_measurement(self):
        data = self.read_data()
        return float(data) * 0.001
