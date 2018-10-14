from space.components.base import MovementComponent
from space.constants.directions import CLOCKWISE


class ReactionWheel(MovementComponent):
    def __init__(self, axis, rotation=CLOCKWISE, *args, **kwargs):
        self._axis = axis
        self.rotation = rotation
        super(ReactionWheel, self).__init__(*args, **kwargs)

    @property
    def axis(self):
        return self._axis

    @property
    def current_acceleration(self):
        acceleration = super(ReactionWheel, self).current_acceleration
        return acceleration if self.rotation == CLOCKWISE else -acceleration
