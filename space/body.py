from vectors import Point
from vectors import Vector

from constants.math import DEGREES_TO_RADIANS
from constants.math import RADIANS


class Body(object):
    def __init__(self, *args, **kwargs):
        self.position = kwargs.pop('position', Point(0, 0, 0))
        self.current_vector = kwargs.pop('current_vector', Vector(0, 0, 0))
        self.mass = kwargs.pop('mass', 0)
        self._yaw_degrees = kwargs.pop('yaw', 0)
        self._roll_degrees = kwargs.pop('roll', 0)
        self._pitch_degrees = kwargs.pop('pitch', 0)
        self._acceleration_vectors = []

    def add_acceleration_vector(self, vector):
        self._acceleration_vectors.append(vector)

    def apply_acceleration_vectors(self):
        for vector in self._acceleration_vectors:
            self.current_vector += vector
        self._acceleration_vectors = []
        self.position += self.current_vector

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
