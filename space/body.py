from vectors import Point
from vectors import Vector

from space.mixins import OrientationMixin


class Body(OrientationMixin):
    def __init__(self, *args, **kwargs):
        self.position = kwargs.pop('position', Point(0, 0, 0))
        self.current_vector = kwargs.pop('current_vector', Vector(0, 0, 0))
        self.mass = kwargs.pop('mass', 0)
        self.yaw_speed = kwargs.pop('yaw_speed', 0)
        self.roll_speed = kwargs.pop('roll_speed', 0)
        self.pitch_speed = kwargs.pop('pitch_speed', 0)
        self._acceleration_vectors = []

    def add_acceleration_vector(self, vector):
        self._acceleration_vectors.append(vector)

    def apply_acceleration_vectors(self):
        for vector in self._acceleration_vectors:
            self.current_vector += vector
        self._acceleration_vectors = []
        self.position += self.current_vector
