__author__ = 'James Myatt'

from ..sensor import SensorInterface, SensorInterfaceFactory
from ..utils import FileAccessWrapper
import os


class Factory(SensorInterfaceFactory):
    def __init__(self):
        dict_if = {
            'file': FileInterface
        }
        SensorInterfaceFactory.__init__(
            self,
            dict_if=dict_if,
            default_if='file',
            default_args={})


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
