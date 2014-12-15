import time

__author__ = 'James Myatt'


class Monitor(object):
    def __init__(self):
        self.name = "Sensor Monitor"
        self._sensors = []
        self._triggers = []
        self._loggers = []
        pass

    def run(self):
        print(self.name)
        while True:
            time.sleep(10)
