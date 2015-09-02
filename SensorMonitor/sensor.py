import SensorMonitor

__author__ = 'James Myatt'


class Factory:
    def __init__(self):
        self.__dict = {}
        self.register('time', SensorMonitor.time.Factory)
        self.register('w1therm', SensorMonitor.w1therm.Factory)

    def register(self, sensor_type, factory_cls):
        self.__dict[sensor_type] = factory_cls

    def create(self, type, **kwargs):
        factory = self.__dict[type]()
        return factory.create(**kwargs)


class SensorFactory:
    def __init__(self, sensor_cls, factory_if):
        self.sensor_cls = sensor_cls
        self.factory_if = factory_if
    
    def create(self, spec=None):
        sensor_if = self.factory_if.create(spec)
        return self.sensor_cls(sensor_if)


class Sensor:
    def __init__(self, sensor_if):
        self.sensor_if = sensor_if

    def get_measurement(self):
        return self.sensor_if.read_data()


class SensorInterfaceFactory:
    def __init__(self, dict_if, default_if=None, default_args=None):
        self.__dict = dict_if

        if default_if is None:
            self.default_if = self.__dict.keys[0]
        else:
            self.default_if = default_if

        if default_args is None:
            self.default_args = {}
        else:
            self.default_args = default_args

    def create(self, interface=None, **kwargs):
        if interface:
            interface_cls = self.__dict[interface]
            return interface_cls(**kwargs)
        else:
            interface_cls = self.__dict[self.default_if]
            return interface_cls(**self.default_args)


class SensorInterface:
    def __init__(self):
        pass

    def read_data(self):
        return None
