__author__ = 'James Myatt'

from ..sensor import SensorInterface
from ..utils import FileAccessWrapper
import os


class Factory:
    def __init__(self):
        self.base_dir = '/sys/bus/w1/devices'

    def create(self, sensor_id=None):
        if not sensor_id:
            device_folder = [x for x in os.listdir(self.base_dir) if x.startswith('28')]
            sensor_id = device_folder[0]

        device_file = self.base_dir + '/' + sensor_id + '/w1_slave'
        return FileInterface(FileAccessWrapper(device_file)), sensor_id


class FileInterface(SensorInterface):
    def __init__(self, file_access):
        SensorInterface.__init__(self)
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
