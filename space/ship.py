from body import Body
from constants.directions import DIRECTIONS


class ShipPanel(object):
    def __init__(self, side, *args, **kwargs):
        self.side = side
        self.thrusters = kwargs.get('thrusters', [])
        for thruster in self.thrusters:
            thruster.attached_panel = self


class Ship(Body):
    def __init__(self, *args, **kwargs):
        self.reaction_wheels = kwargs.pop('reaction_wheels', [])
        self.panels = {
            side: kwargs.pop("{}_panel".format(side), ShipPanel(side=side))
            for side in DIRECTIONS
        }
        for panel in self.panels.values():
            panel.attached_body = self
        super(Ship, self).__init__(*args, **kwargs)

    @property
    def thrusters(self):
        return [thruster for panel in self.panels.values()
                for thruster in panel.thrusters]

    @property
    def active_thrusters(self):
        return [c for c in self.thrusters if c.is_active]

    def apply_acceleration_vectors(self):
        self._apply_thrust()
        self.position += self.current_vector

    def _apply_thrust(self):
        for thruster in self.active_thrusters:
            self.current_vector += thruster.acceleration_vector
