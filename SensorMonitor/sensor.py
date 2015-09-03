import SensorMonitor


class SensorFactory:
    def __init__(self, sensor_cls, factory_if):
        self.sensor_cls = sensor_cls
        self.factory_if = factory_if

    def create(self, **kwargs):
        sensor_if = self.factory_if.create(**kwargs)
        return self.sensor_cls(sensor_if)


class Sensor:
    def __init__(self, sensor_if):
        self.sensor_if = sensor_if

    def get_measurement(self):
        return self.sensor_if.read_data()


class SensorInterfaceFactory:
    def __init__(self, default_if=None, default_args=None):
        self.__dict = {}
        self.default_if = default_if

        if default_args is None:
            self.default_args = {}
        else:
            self.default_args = default_args

    def register(self, interface, interface_cls):
        self.__dict[interface] = interface_cls
        if not self.default_if:
            self.default_if = interface

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
