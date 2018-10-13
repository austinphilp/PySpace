from constants.directions import DIRECTIONAL_VECTORS
from constants.math import DEGREES_TO_RADIANS
from constants.math import RADIANS
from vectors import Vector


class Body(object):
    def __init__(self, current_vector, point, mass, yaw, roll, pitch):
        self.position = point
        self._yaw_degrees = yaw
        self._roll_degrees = roll
        self._pitch_degrees = pitch
        self._accelleration_vectors = []

    def get_yaw(self, unit_type):
        if unit_type == RADIANS:
            return self._yaw_degrees * DEGREES_TO_RADIANS
        else:
            return self._yaw_degrees

    def get_pitch(self, unit_type):
        if unit_type == RADIANS:
            return self._pitch_degrees * DEGREES_TO_RADIANS
        else:
            return self._pitch_degrees

    def get_roll(self, unit_type):
        if unit_type == RADIANS:
            return self._roll_degrees * DEGREES_TO_RADIANS
        else:
            return self._roll_degrees

    def _create_accelleration_vector(
            self,
            direction,
            acceleration,
            roll=None,
            pitch=None,
            yaw=None):
        vector = Vector.from_list(
            [x * acceleration for x in DIRECTIONAL_VECTORS[direction]]
        )
        # Rotate by Roll
        vector = vector.rotate(roll or self.get_roll(RADIANS), (1, 0, 0))
        # Rotate by Pitch
        vector = vector.rotate(pitch or self.get_pitch(RADIANS), (0, 1, 0))
        # Rotate by Yaw
        vector = vector.rotate(yaw or self.get_yaw(RADIANS), (0, 0, 1))

        return vector

