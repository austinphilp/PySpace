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
        force /= getattr(self.attached_body, 'mass', 1)
        return force if self.rotation == CLOCKWISE else -force

    @property
    def status_report(self):
        return {
            **super(ReactionWheel, self).status_report,
            "current_acceleration": self.current_acceleration,
            "axis": self.axis,
            "rotation": self.rotation,
            "mass": self.mass
        }
