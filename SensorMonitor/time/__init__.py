__author__ = 'James Myatt'

__all__ = ['interface']

from ..sensor import Sensor, SensorFactory
import interface


class Factory(SensorFactory):
    def __init__(self, factory=None):
        if not factory:
            factory = interface.Factory()
        SensorFactory.__init__(self, Time, factory)


class Time(Sensor):
    def __init__(self, sensor_if):
        Sensor.__init__(self, sensor_if)
