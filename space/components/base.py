from abc import ABC

from space.utils.sanitization import sanitize_integrity
from space.utils.sanitization import sanitize_throttle


class BaseComponent(ABC):
    def __init__(self, *args, **kwargs):
        self._integrity = 1.0
        self.attached_body = kwargs.get('attached_body')
        self.attached_panel = kwargs.get('attached_panel')

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

    @property
    def position(self):
        return self.attached_body.position

    @property
    def status_report(self):
        return {
            "integrity": self.integrity,
            "is_acitve": self.is_active,
        }

    def degrade(self, amount):
        self.integrity -= amount
        return self.integrity

    def repair(self, amount):
        self.integrity += amount
        return self.integrity


class PoweredComponent(BaseComponent):
    def __init__(self, *args, **kwargs):
        BaseComponent.__init__(self, *args, **kwargs)
        self.powered_on = kwargs.get('powered_on', True)
        super(PoweredComponent, self).__init__(self, *args, **kwargs)

    @property
    def power_consumption(self):
        return 0

    @property
    def is_active(self):
        return super(PoweredComponent, self).is_active and self.powered_on

    @property
    def status_report(self):
        return {
            "integrity": self.integrity,
            "is_active": self.is_active,
            "powered_on": self.powered_on,
            "power_consumption": self.power_consumption,
        }


class MovementComponent(PoweredComponent):
    def __init__(self, max_force, *args, **kwargs):
        PoweredComponent.__init__(self, *args, **kwargs)
        self.initial_max_force = max_force
        self._throttle = 0

    @property
    def throttle(self):
        return self._throttle

    @property
    def power_adjusted_current_force(self):
        return (
            self.current_force *
            getattr(self.attached_body, 'overall_performance_modifier', 1)
        )

    @throttle.setter
    def throttle(self, throttle):
        self._throttle = sanitize_throttle(throttle)

    @property
    def degredation_rate(self):
        return max(0, self._throttle-1) / 5000

    @property
    def status_report(self):
        return {
            **super(MovementComponent, self).status_report,
            "throttle": self.throttle,
            "current_force": self.power_adjusted_current_force,
            "degredation_rate": self.degredation_rate,
            "max_force": self.max_force
        }

    def apply_degredation(self):
        self.integrity = round(max(0, self.integrity-self.degredation_rate), 5)

    @property
    def max_force(self):
        return self.integrity * self.initial_max_force

    @property
    def current_force(self):
        return self.max_force * self.throttle

    @property
    def power_consumption(self):
        return self.current_force
