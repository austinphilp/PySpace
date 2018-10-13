from constants.math import DEGREES_TO_RADIANS
from constants.math import RADIANS


class Body(object):
    def __init__(self, current_vector, point, mass, yaw, roll, pitch):
        self.position = point
        self._yaw_degrees = yaw
        self._roll_degrees = roll
        self._pitch_degrees = pitch
        self._acceleration_vectors = []

    def add_acceleration_vector(self, vector):
        self._acceleration_vectors.append(vector)

    def get_yaw(self, unit_type=RADIANS):
        if unit_type == RADIANS:
            return self._yaw_degrees * DEGREES_TO_RADIANS
        else:
            return self._yaw_degrees

    def get_pitch(self, unit_type=RADIANS):
        if unit_type == RADIANS:
            return self._pitch_degrees * DEGREES_TO_RADIANS
        else:
            return self._pitch_degrees

    def get_roll(self, unit_type=RADIANS):
        if unit_type == RADIANS:
            return self._roll_degrees * DEGREES_TO_RADIANS
        else:
            return self._roll_degrees
