__author__ = 'James Myatt'

from ..sensor import SensorInterface
from ..utils import FileAccessWrapper
import os


class Factory:
    def __init__(self):
        self.__dict = {
            'file': FileInterface
            }
        self.default_if = 'file'
        self.default_args = {}

    def create(self, spec):
        if spec['interface']:
            interface_cls = self.__dict[spec['interface']]
            return interface_cls(**spec['args'])
        else:
            interface_cls = self.__dict[self.default_if]
            return interface_cls(**self.default_args)


class FileInterface(SensorInterface):
    def __init__(self, sensor_id=None, file_access=None, **kwargs):
        SensorInterface.__init__(self)
        if not file_access:
            if not sensor_id:
                device_folder = [x for x in os.listdir('/sys/bus/w1/devices/') if x.startswith('28')]
                sensor_id = device_folder[0]

             device_file = '/sys/bus/w1/devices/' + sensor_id + '/w1_slave'
             file_access = FileAccessWrapper(device_file)
             
         self.file_access = file_access

    def read_data(self):
        with self.file_access.open() as f:
            line = f.readline().strip()
            if not line or not line.endswith('YES'):
                return None

            line = f.readline().strip()
            if not line or 't=' not in line:
                return None

        return line.split('=')[1]
