from space.body import Body
from space.constants.directions import DIRECTIONS


class ShipPanel(object):
    def __init__(self, side, *args, **kwargs):
        self.side = side
        self.thrusters = kwargs.get('thrusters', [])
        for thruster in self.thrusters:
            thruster.attached_panel = self
        self.mass = sum(t.mass for t in self.thrusters)


class Ship(Body):
    def __init__(self, *args, **kwargs):
        super(Ship, self).__init__(*args, **kwargs)
        self.reaction_wheels = kwargs.pop('reaction_wheels', [])
        self.panels = {
            side: kwargs.pop(F"{side}_panel", ShipPanel(side=side))
            for side in DIRECTIONS
        }
        for obj in self.reaction_wheels + list(self.panels.values()):
            obj.attached_body = self

        self.mass += (
            sum(r.mass for r in self.reaction_wheels) +
            sum(p.mass for p in self.panels.values())
        )

    @property
    def thrusters(self):
        return [thruster for panel in self.panels.values()
                for thruster in panel.thrusters]

    def get_thrusters_by_orientation(self, orientation):
        return [t for t in self.thrusters if t.direction == orientation]

    def apply_acceleration_vectors(self):
        self._apply_thrust()
        self._apply_rotation()
        self.position += self.current_vector

    def _apply_rotation(self):
        self._update_rotational_speed()
        self.yaw_degrees += self.yaw_speed
        self.roll_degrees += self.roll_speed
        self.pitch_degrees += self.pitch_speed

    def _update_rotational_speed(self):
        for wheel in self.reaction_wheels:
            if wheel.is_active:
                rotational_speed = getattr(self, F"{wheel.axis}_speed")
                rotational_speed += wheel.current_acceleration
                setattr(self, F"{wheel.axis}_speed", rotational_speed)

    def _apply_thrust(self):
        for thruster in [t for t in self.thrusters]:
            if thruster.is_active:
                self.current_vector += thruster.acceleration_vector
