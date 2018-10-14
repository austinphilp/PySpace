from components.base import MovementComponent
from constants.directions import COUNTER_DIRECTIONS
from constants.directions import DIRECTIONAL_VECTORS
from utils.vectors import round_point


class Thruster(MovementComponent):
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

        vector = DIRECTIONAL_VECTORS[self.direction]
        # Rotate by Roll
        vector = round_point(vector.rotate(self.get_roll(), (1, 0, 0)))
        # Rotate by Pitch
        vector = round_point(vector.rotate(self.get_pitch(), (0, 1, 0)))
        # Rotate by Yaw
        vector = round_point(vector.rotate(self.get_yaw(), (0, 0, 1)))
        return vector

    @property
    def acceleration_vector(self):
        return round_point(
            self._directional_vector.multiply(self.current_acceleration)
        )

    def get_roll(self, *args, **kwargs):
        return self.attached_panel.attached_body.get_roll(*args, **kwargs)

    def get_yaw(self, *args, **kwargs):
        return self.attached_panel.attached_body.get_yaw(*args, **kwargs)

    def get_pitch(self, *args, **kwargs):
        return self.attached_panel.attached_body.get_pitch(*args, **kwargs)