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
        self.register('fake', FakeInterface)


class SystemInterface(SensorInterface):
    def __init__(self):
        SensorInterface.__init__(self)

    def read_data(self):
        return time.time()


class FakeInterface(SensorInterface):
    def __init__(self, output=0, **kwargs):
        SensorInterface.__init__(self)
        self.__output = output

    def read_data(self):
        return self.__output
