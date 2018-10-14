from space.components.base import MovementComponent


class ReactionWheel(MovementComponent):
    def __init__(self, axis, *args, **kwargs):
        self.axis = axis
        super(ReactionWheel, self).__init__(*args, **kwargs)

    def apply_acceleration(self):
        current_rotational_speed = getattr(
            self.attached_body,
            "{}_speed".format(self.axis)
        )
        setattr(
            self.attached_body,
            "{}_speed".format(self.axis),
            current_rotational_speed + self.current_acceleration
        )
