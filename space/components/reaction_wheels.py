from space.components.base import MovementComponent
from space.constants.directions import CLOCKWISE
from space.constants.ratios import KG_PER_RW_ACC


class ReactionWheel(MovementComponent):
    def __init__(self, axis, rotation=CLOCKWISE, *args, **kwargs):
        MovementComponent.__init__(self, *args, **kwargs)
        self._axis = axis
        self.rotation = rotation
        self.mass = self.initial_max_force * KG_PER_RW_ACC

    @property
    def axis(self):
        return self._axis

    @property
    def current_acceleration(self):
        force = super(ReactionWheel, self).current_force
        return force if self.rotation == CLOCKWISE else -force
