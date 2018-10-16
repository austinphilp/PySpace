from vectors import Vector


def apply_acceleration_to_vector(self, vector, acceleration):
    return Vector.from_list([x * self.current_acceleration for x in vector])


def round_point(point):
    point.x = point.x
    point.y = point.y
    point.z = point.z
    return point
