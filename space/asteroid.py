from random import normalvariate
from vectors import Vector

from space.body import Body
from space.mixins import IdentityMixin, OrientationMixin


class Asteroid(Body, IdentityMixin):
    def __init__(self, *args, **kwargs):
        super(Asteroid, self).__init__(*args, **kwargs)
        OrientationMixin.__init__(self, *args, **kwargs)
        self.mass = kwargs.get('mass')
        self.current_vector = kwargs.get('vector')
        # TODO(Austin) - Density of materials Determines size according to mass
        self.height = self.mass/250 * normalvariate(1, 0.2)
        self.width = self.mass/250 * normalvariate(1, 0.2)
        self.depth = self.mass/250 * normalvariate(1, 0.2)
        self.current_acceleration = Vector(0, 0, 0)
