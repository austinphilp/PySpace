from random import normalvariate
from vectors import Vector

from space.body import Body
from space.mixins import IdentityMixin, OrientationMixin


class Station(Body, IdentityMixin):
    def __init__(self, *args, **kwargs):
        super(Station, self).__init__(*args, **kwargs)
        OrientationMixin.__init__(self, *args, **kwargs)
        self.mass = kwargs.get('base_mass')
        self.height = self.mass/25 * normalvariate(1, 0.2)
        self.width = self.mass/25 * normalvariate(1, 0.2)
        self.depth = self.mass/25 * normalvariate(1, 0.2)
        self.current_acceleration = Vector(0, 0, 0)
        self.current_vector = Vector(0, 0, 0)
