import time

__author__ = 'James Myatt'


class Monitor(object):
    def __init__(self):
        self.name = "Sensor Monitor"
        self.__sensors = []
        self.__triggers = []
        self.__loggers = []
    
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
        while True:
            time.sleep(10)
