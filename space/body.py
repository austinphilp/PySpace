from vectors import Point
from vectors import Vector

from space.constants.math import DEGREES_TO_RADIANS
from space.constants.math import RADIANS


class Body(object):
    def __init__(self, *args, **kwargs):
        self.position = kwargs.pop('position', Point(0, 0, 0))
        self.current_vector = kwargs.pop('current_vector', Vector(0, 0, 0))
        self.mass = kwargs.pop('mass', 0)
        self.yaw_degrees = kwargs.pop('yaw', 0)
        self.yaw_speed = kwargs.pop('yaw_speed', 0)
        self.roll_degrees = kwargs.pop('roll', 0)
        self.roll_speed = kwargs.pop('roll_speed', 0)
        self.pitch_degrees = kwargs.pop('pitch', 0)
        self.pitch_speed = kwargs.pop('pitch_speed', 0)
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
            return self.yaw_degrees * DEGREES_TO_RADIANS
        else:
            return self.yaw_degrees

    def get_pitch(self, unit_type=RADIANS):
        if unit_type == RADIANS:
            return self.pitch_degrees * DEGREES_TO_RADIANS
        else:
            return self.pitch_degrees

    def get_roll(self, unit_type=RADIANS):
        if unit_type == RADIANS:
            return self.roll_degrees * DEGREES_TO_RADIANS
        else:
            return self.roll_degrees
