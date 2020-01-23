from space.components.base import MovementComponent
from space.constants.directions import COUNTER_DIRECTIONS
from space.constants.directions import DIRECTIONAL_VECTORS
from space.constants.ratios import KG_PER_THRUSTER_ACC
from space.utils.vectors import round_point


class Thruster(MovementComponent):
    def __init__(self, *args, **kwargs):
        MovementComponent.__init__(self, *args, **kwargs)
        self.mass = self.initial_max_force * KG_PER_THRUSTER_ACC

    @property
    def direction(self):
        return COUNTER_DIRECTIONS[self.attached_panel.side]

    @property
    def _directional_vector(self):
        # TODO(Austin) - Find out if this is equivalent to a unit vector
        """Return a vector for the thrust direction

        taking into account the current orientation of the attached body,
        with an acceleration value of 1, to be used in the calculation of
        the acceleration vector, by multiplying this vector by accelleration
        """

        return self.attached_body.rotate_vector_by_orientation(
            vector=DIRECTIONAL_VECTORS[self.direction],
        )

    @property
    def attached_body(self):
        return getattr(self.attached_panel, 'attached_body', None)

    @attached_body.setter
    def attached_body(self, body):
        pass

    @property
    def acceleration_vector(self):
        return round_point(
            self._directional_vector.multiply(self.current_acceleration)
        )

    @property
    def current_acceleration(self):
        return self.power_adjusted_current_force/self.attached_body.mass

    @property
    def status_report(self):
        return {
            **super().status_report,
            "direction": self.direction,
            "acceleration_vector": {
                "x": self.acceleration_vector.x,
                "y": self.acceleration_vector.y,
                "z": self.acceleration_vector.z,
            },
            "current_acceleration": self.current_acceleration,
            "current_force": self.power_adjusted_current_force,
            "mass": self.mass
        }
