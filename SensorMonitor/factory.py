import SensorMonitor


class Factory:
    def __init__(self):
        self.__dict = {}
        self.register('time', SensorMonitor.time.Factory)
        self.register('w1therm', SensorMonitor.w1therm.Factory)

    def register(self, type, factory_cls):
        self.__dict[type] = factory_cls

    def create(self, type, **kwargs):
        factory = self.__dict[type]()
        return factory.create(**kwargs)
