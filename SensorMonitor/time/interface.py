from ..sensor import SensorInterface, SensorInterfaceFactory
import time

__author__ = 'James Myatt'


class Factory(SensorInterfaceFactory):
    def __init__(self):
        SensorInterfaceFactory.__init__(
            self,
            default_if='system',
            default_args={})
        self.register('system', SystemInterface)


class SystemInterface(SensorInterface):
    def __init__(self):
        SensorInterface.__init__(self)

    def read_data(self):
        return time.time()
