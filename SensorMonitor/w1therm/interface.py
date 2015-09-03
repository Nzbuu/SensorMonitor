from ..sensor import SensorInterface, SensorInterfaceFactory
from ..utils import FileAccessWrapper
import os

__author__ = 'James Myatt'


class Factory(SensorInterfaceFactory):
    def __init__(self):
        SensorInterfaceFactory.__init__(
            self,
            default_if='file',
            default_args={})
        self.register('file', FileInterface)
        self.register('fake', FakeInterface)


class FileInterface(SensorInterface):
    def __init__(self, sensor_id=None, sensor_type=None, base_dir='/sys/bus/w1/devices', file_access=None, **kwargs):
        SensorInterface.__init__(self)

        if not file_access:
            if not sensor_id:
                sensor_id = FileInterface.detect_file(base_dir=base_dir, sensor_type=sensor_type)

            device_file = os.path.join(base_dir, sensor_id, 'w1_slave')
            file_access = FileAccessWrapper(device_file)

        self.sensor_id = sensor_id
        self.file_access = file_access

    def read_data(self):
        with self.file_access.open() as f:
            line = f.readline().strip()
            if not line or not line.endswith('YES'):
                return None

            line = f.readline().strip()
            if not line or 't=' not in line:
                return None

        return float(line.split('=')[1])

    @classmethod
    def detect_file(cls, base_dir='/sys/bus/w1/devices', sensor_type=None):
        device_folder = [x for x in os.listdir(base_dir) if x.startswith('28')]
        return device_folder[0]


class FakeInterface(SensorInterface):
    def __init__(self, output=0, **kwargs):
        SensorInterface.__init__(self)
        self.__output = output

    def read_data(self):
        return self.__output
