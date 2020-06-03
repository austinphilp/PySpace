from math import sqrt
from vectors import Vector

from space.constants.math import PRECISION


def apply_acceleration_to_vector(self, vector, acceleration):
    return Vector.from_list([x * self.current_acceleration for x in vector])


def square_distance(point_1, point_2):
    if isinstance(point_1, list) or isinstance(point_1, tuple):
        x1, y1, z1 = point_1
    else:
        x1, y1, z1 = point_1.x, point_1.y, point_1.z

    if isinstance(point_2, list) or isinstance(point_2, tuple):
        x2, y2, z2 = point_2
    else:
        x2, y2, z2 = point_2.x, point_2.y, point_2.z

    return (
        ((x2 - x1)**2) +
        ((y2 - y1)**2) +
        ((z2 - z1)**2)
    )


def get_distance(point_1, point_2):
    return sqrt(square_distance(point_1, point_2))


def round_point(point):
    point.x = round(point.x, PRECISION)
    point.y = round(point.y, PRECISION)
    point.z = round(point.z, PRECISION)
    return point


def rotate_vector(vector, roll, pitch, yaw):
    # Rotate by Roll
    vector = round_point(vector.rotate(roll, (1, 0, 0)))
    # Rotate by Pitch
    vector = round_point(vector.rotate(pitch, (0, 1, 0)))
    # Rotate by Yaw
    vector = round_point(vector.rotate(yaw, (0, 0, 1)))
    return vector
