from space.components.base import PoweredComponent


class Sensor(PoweredComponent):
    def __init__(self, base_range, *args, **kwargs):
        PoweredComponent.__init__(self, *args, **kwargs)
        self.base_range = base_range
