from ..sensor import SensorInterface, SensorInterfaceFactory
from datetime import datetime


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
        return datetime.utcnow()


class FakeInterface(SensorInterface):
    def __init__(self, output=None, **kwargs):
        SensorInterface.__init__(self)
        if output:
            self.__output = output
        else:
            self.__output = datetime.utcfromtimestamp(0)

    def read_data(self):
        return self.__output
