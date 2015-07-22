__author__ = 'James'

import os


class Sensor:
    def __init__(self):
        pass


class DS18B20(Sensor):
    def __init__(self, sensor_id=''):
        Sensor.__init__(self)
        self.sensorID = sensor_id

        self.base_dir = '/sys/bus/w1/devices'
        self.device_file = ''

    def init_sensor(self):
        if not self.device_file:
            if not self.sensorID:
                device_folder = [x for x in os.listdir(self.base_dir) if x.startswith('28')]
                self.sensorID = device_folder[0]
            self.device_file = self.base_dir + '/' + self.sensorID + '/w1_slave'

    def read_sensor(self):
        self.init_sensor()

        with open(self.device_file, 'rb') as f:
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
