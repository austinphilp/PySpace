from space.constants.math import PRECISION
from vectors import Vector


def apply_acceleration_to_vector(self, vector, acceleration):
    return Vector.from_list([x * self.current_acceleration for x in vector])


def round_point(point):
    point.x = round(point.x, PRECISION)
    point.y = round(point.y, PRECISION)
    point.z = round(point.z, PRECISION)
    return point
