__author__ = 'James'

import os

class Sensor:
    def __init__(self):
        pass


class FileAccessWrapper:
    def __init__(self, filename):
        self.filename = filename

    def open(self):
        return open(self.filename, 'r')


class W1ThermFactory:
    def __init__(self):
        self.base_dir = '/sys/bus/w1/devices'

    def create(self, sensor_id=None):
        if not sensor_id:
            device_folder = [x for x in os.listdir(self.base_dir) if x.startswith('28')]
            sensor_id = device_folder[0]

        device_file = self.base_dir + '/' + sensor_id + '/w1_slave'
        return W1Therm(sensor_id=sensor_id, file_access=FileAccessWrapper(device_file))


class W1Therm(Sensor):
    def __init__(self, sensor_id='', file_access=None):
        Sensor.__init__(self)
        self.sensor_id = sensor_id
        self.file_access = file_access

    def read_sensor(self):
        with self.file_access.open() as f:
            line = f.readline().strip()
            if not line or not line.endswith('YES'):
                return None

            line = f.readline().strip()
            if not line or 't=' not in line:
                return None

            return float(line.split('=')[1]) * 0.001

    def get_measurement(self):
        data = self.read_sensor()
        return data
