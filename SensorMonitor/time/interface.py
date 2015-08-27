__author__ = 'James Myatt'

from ..sensor import SensorInterface, SensorInterfaceFactory
import time


class Factory(SensorInterfaceFactory):
    def __init__(self):
        dict_if = {
            'system': SystemInterface
        }
        SensorInterfaceFactory.__init__(
            self,
            dict_if=dict_if,
            default_if='system',
            default_args={})


class SystemInterface(SensorInterface):
    def __init__(self):
        SensorInterface.__init__(self)

    def read_data(self):
        return time.time()
