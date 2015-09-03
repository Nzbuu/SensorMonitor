from ..sensor import Sensor, SensorFactory
from . import interface

__author__ = 'James Myatt'
__all__ = ['interface', 'Factory', 'Time']


class Factory(SensorFactory):
    def __init__(self, factory=None):
        if not factory:
            factory = interface.Factory()
        SensorFactory.__init__(self, Time, factory)


class Time(Sensor):
    def __init__(self, sensor_if):
        Sensor.__init__(self, sensor_if)
