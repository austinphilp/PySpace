from vectors import Vector


def apply_acceleration_to_vector(self, vector, acceleration):
    return Vector.from_list([x * self.current_acceleration for x in vector])
