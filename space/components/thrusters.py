from components.base import MovementComponent
from constants.directions import DIRECTIONAL_VECTORS


class Thruster(MovementComponent):
    def __init__(self, direction_of_thrust, *args, **kwargs):
        self.direction = direction_of_thrust
        super(Thruster, self).__init__(*args, **kwargs)

    @property
    def _directional_vector(self):
        # TODO(Austin) - Find out if this is equivalent to a unit vector
        """Return a vector for the thrust direction

        taking into account the current orientation of the attached body,
        with an acceleration value of 1, to be used in the calculation of
        the acceleration vector, by multiplying this vector by accelleration
        """

        vector = DIRECTIONAL_VECTORS[self.direction]
        # Rotate by Roll
        vector = vector.rotate(self.attached_body.get_roll(), (1, 0, 0))
        # Rotate by Pitch
        vector = vector.rotate(self.attached_body.get_pitch(), (0, 1, 0))
        # Rotate by Yaw
        vector = vector.rotate(self.attached_body.get_yaw(), (0, 0, 1))

    def apply_acceleration(self):
        acceleration_vector = self._directional_vector.multiply(
            self.current_acceleration
        )
        self.attached_body.add_acceleration_vector(acceleration_vector)
