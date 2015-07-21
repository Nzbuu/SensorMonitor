from datetime import datetime
import time

__author__ = 'James Myatt'


class Monitor(object):
    def __init__(self):
        self.name = "Sensor Monitor"
        self.__sensors = []
        self.__triggers = []
        self.__loggers = []
        self.time_step = 1
        self.num_stop = 5
        self.__count_meas = 0

    def __del__(self):
        pass

    def add_sensor(self, sensor):
        self.__sensors.append(sensor)

    def add_trigger(self, trigger):
        self.__triggers.append(trigger)

    def add_logger(self, logger):
        self.__loggers.append(logger)

    def run(self):
        print(self.name)
        while self.__count_meas < self.num_stop:
            result = self.get_measurements()
            self.store_measurements(result)
            self.__count_meas += 1
            time.sleep(self.time_step)

    def get_measurements(self):
        result = {'timestamp': datetime.now()}
        for sensor in self.__sensors:
            sensor_data = sensor.get_measurement()
            result[sensor.identifier] = sensor_data
        return result

    def store_measurements(self, result):
        print("Sample", result['timestamp'])
        for logger in self.__loggers:
            logger.store_measurement(result)
