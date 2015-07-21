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

        with open(self.device_file, 'r') as f:
            raw_data = f.read()

        raw_data = self.parse_data(raw_data)
        return raw_data

    def parse_data(self, raw_data):
        raw_data = raw_data.split('\n')
        if raw_data[0].endswith('YES'):
            return float(raw_data[1].split('=')[1]) * 0.001
        else:
            return None

    def get_measurement(self):
        data = self.read_sensor()
        return data
