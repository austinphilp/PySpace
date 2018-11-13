from math import sqrt
from vectors import Vector

from space.constants.math import PRECISION


def apply_acceleration_to_vector(self, vector, acceleration):
    return Vector.from_list([x * self.current_acceleration for x in vector])


def get_distance(point_1, point_2):
    return sqrt(
        ((point_2.x - point_1.y)**2) +
        ((point_2.y - point_1.y)**2) +
        ((point_2.z - point_1.z)**2)
    )


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
