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
        self.integrity = 1.0
        self._acceleration_vectors = []

    def add_acceleration_vector(self, vector):
        self._acceleration_vectors.append(vector)

    def apply_acceleration_vectors(self):
        for vector in self._acceleration_vectors:
            self.current_vector += vector
        self._acceleration_vectors = []
        self.position += self.current_vector

    def perform_collision(self, other_body, perform_on_other=True):
        force = other_body.mass * (
            self.current_vector
            - other_body.current_vector
        ).magnitude()
        self.integrity = max(self.integrity - force/self.mass, 0)
        self.current_vector = self.current_vector.multiply(-1)
        other_body.perform_collision(self, perform_on_other=False)

    def is_colliding(self, other_body):
        # TODO(Austin) - Refactor, this code is bad and you should feel bad
        a_x1 = self.position.x - (self.width/2)
        a_x2 = self.position.x + (self.width/2)
        a_y1 = self.position.y - (self.depth/2)
        a_y2 = self.position.y + (self.depth/2)
        a_z1 = self.position.z - (self.height/2)
        a_z2 = self.position.z + (self.height/2)
        b_x1 = other_body.position.x - (other_body.width/2)
        b_x2 = other_body.position.x + (other_body.width/2)
        b_y1 = other_body.position.y - (other_body.depth/2)
        b_y2 = other_body.position.y + (other_body.depth/2)
        b_z1 = other_body.position.z - (other_body.height/2)
        b_z2 = other_body.position.z + (other_body.height/2)
        return not a_x2 < b_x1 and \
            not b_x2 < a_x1 and \
            not a_y2 < b_y1 and \
            not b_y2 < a_y1 and \
            not a_z2 < b_z1 and \
            not b_z2 < a_z1
