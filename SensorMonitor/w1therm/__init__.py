from ..sensor import Sensor, SensorFactory
from . import interface

__author__ = 'James Myatt'
__all__ = ['interface', 'Factory', 'W1Therm']


class Factory(SensorFactory):
    def __init__(self, factory=None):
        if not factory:
            factory = interface.Factory()
        SensorFactory.__init__(self, W1Therm, factory)


class W1Therm(Sensor):
    def __init__(self, sensor_if):
        Sensor.__init__(self, sensor_if)

    def get_measurement(self):
        data = self.sensor_if.read_data()
        if data:
            return data * 0.001
        else:
            return data
