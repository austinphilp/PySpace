from constants.directions import DIRECTIONAL_VECTORS
from constants.math import DEGREES_TO_RADIANS
from constants.math import RADIANS
from vectors import Vector


class Body(object):
    def __init__(self, current_vector, point, yaw, roll, pitch):
        self.position = point
        self._yaw = yaw
        self._roll = roll
        self._pitch = pitch
        self._accelleration_vectors = []

    def get_yaw(self, unit_type):
        if unit_type == RADIANS:
            return self._yaw * DEGREES_TO_RADIANS
        else:
            return self._yaw

    def get_pitch(self, unit_type):
        if unit_type == RADIANS:
            return self._pitch * DEGREES_TO_RADIANS
        else:
            return self._pitch

    def get_roll(self, unit_type):
        if unit_type == RADIANS:
            return self._roll * DEGREES_TO_RADIANS
        else:
            return self._roll

    def accellerate(self, direction, acceleration):
        vector = Vector.from_list(
            [x * direction for x in DIRECTIONAL_VECTORS[direction]]
        )
        # Rotate by Roll
        vector = vector.rotate(self.get_roll(RADIANS), (1, 0, 0))
        # Rotate by Pitch
        vector = vector.rotate(self.get_roll(RADIANS), (0, 1, 0))
        # Rotate by Yaw
        vector = vector.rotate(self.get_roll(RADIANS), (0, 0, 1))

        return vector

    def roll(self, acceleration):
        self.roll += acceleration

    def yaw(self, acceleration):
        self.yaw += acceleration

    def pitch(self, acceleration):
        self.pitch += acceleration
