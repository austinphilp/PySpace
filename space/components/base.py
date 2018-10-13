from abc import ABC
from abc import abstractmethod
from decimal import Decimal

from utils.sanitization import sanitize_integrity
from utils.sanitization import sanitize_throttle


class BaseComponent(ABC):
    def __init__(self, *args, **kwargs):
        self._integrity = Decimal('1.0', decimal_places=4, max_digits=5)

    @property
    def is_active(self):
        return self.integrity > 0

    @property
    def integrity(self):
        return self._integrity

    @integrity.setter
    def integrity(self, x):
        self._integrity = sanitize_integrity(x)

    @property
    def degredation_rate(self):
        return 0

    def degrade(self, amount):
        self.integrity -= amount
        return self.integrity

    def repair(self, amount):
        self.integrity += amount
        return self.integrity


class PoweredComponent(BaseComponent):
    def __init__(self, *args, **kwargs):
        self.powered_on = kwargs.get('powered_on', True)
        return super(PoweredComponent, self).__init__(*args, **kwargs)

    @property
    def is_active(self):
        return super(PoweredComponent, self).is_active and self.powered_on


class MovementComponent(PoweredComponent):
    def __init__(self, *args, **kwargs):
        self.initial_max_acceleration = kwargs.pop('max_acceleration')
        self._throttle = 0
        return super(MovementComponent, self).__init__(*args, **kwargs)

    @property
    def throttle(self):
        return self._throttle

    @throttle.setter
    def throttle(self, throttle):
        self._throttle = sanitize_throttle(throttle)

    @property
    def degredation_rate(self):
        return max(Decimal(0), self._throttle-1) / 100

    @property
    def max_acceleration(self):
        return self.integrity * self.initial_max_acceleration

    @property
    def current_acceleration(self):
        return self.max_acceleration * self.throttle

    @abstractmethod
    def apply_acceleration(self):
        pass
