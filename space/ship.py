from space.body import Body
from space.constants.directions import DIRECTIONS
from space.constants.math import DEGREES
from space.mixins import IdentityMixin, OrientationMixin
from space.utils.vectors import rotate_vector


class ShipPanel(IdentityMixin):
    def __init__(self, side, *args, **kwargs):
        self.side = side
        self.thrusters = kwargs.get('thrusters', [])
        self.sensors = kwargs.get('sensors', [])
        self.mining_lasers = kwargs.get('mining_lasers', [])
        for component in (self.thrusters + self.sensors + self.mining_lasers):
            component.attached_panel = self
        self.mass = sum(t.mass for t in self.thrusters)

    @property
    def status_report(self):
        return {
            "object_id": self.object_id,
            "side": self.side,
            "thrusters": [t.status_report for t in self.thrusters],
            "sensors": [s.status_report for s in self.sensors],
            "mass": self.mass
        }

    def get_all_parts(self):
        return {
            part.object_id for part in [self.thrusters, self.sensors]
        }


class Ship(Body, OrientationMixin, IdentityMixin):
    def __init__(self, *args, **kwargs):
        super(Ship, self).__init__(*args, **kwargs)
        OrientationMixin.__init__(self, *args, **kwargs)
        self.reaction_wheels = kwargs.pop('reaction_wheels', [])
        self.reactors = kwargs.pop('reactors', [])
        self.panels = {
            side: kwargs.pop(F"{side}_panel", ShipPanel(side=side))
            for side in DIRECTIONS
        }
        for panel in self.panels.values():
            panel.ship = self
        for obj in self.reaction_wheels + list(self.panels.values()):
            obj.attached_body = self
        self.mass += self._calculate_mass()
        self.height, self.width, self.depth = self._calculate_dimensions()
        self.storage = 0

    def _calculate_dimensions(self):
        # For now all ships will simply be squares
        width = self.mass/25
        height = width
        depth = width
        return height, width, depth

    def _calculate_mass(self):
        components = self.reaction_wheels + \
                     self.reactors + \
                     list(self.panels.values())
        return sum(c.mass for c in components)

    @property
    def power_available(self):
        return sum(r.current_output for r in self.reactors)

    @property
    def power_consumption(self):
        return (
            sum(t.power_consumption
                for t in self.thrusters)
            + sum(r.power_consumption
                  for r in self.reaction_wheels)
            + sum(r.power_consumption
                  for r in self.sensors)
        )

    @property
    def overall_performance_modifier(self):
        if self.power_consumption == 0:
            return 1
        return min(
            1,
            self.power_available/self.power_consumption
        ) * self.integrity

    @property
    def sensors(self):
        return [sensor for panel in self.panels.values()
                for sensor in panel.sensors]

    @property
    def thrusters(self):
        return [thruster for panel in self.panels.values()
                for thruster in panel.thrusters]

    @property
    def current_acceleration(self):
        acceleration = None
        for thruster in self.thrusters:
            if thruster.is_active:
                if acceleration is None:
                    acceleration = thruster.acceleration_vector
                else:
                    acceleration += thruster.acceleration_vector
        return acceleration

    @property
    def status_report(self):
        return {
            "mass": self.mass,
            "object_id": self.object_id,
            "vector": {
                "x": self.current_vector.x,
                "y": self.current_vector.y,
                "z": self.current_vector.z,
            },
            "acceleration": {
                "x": self.current_acceleration.x,
                "y": self.current_acceleration.y,
                "z": self.current_acceleration.z,
            },
            "position": {
                "x": self.position.x,
                "y": self.position.y,
                "z": self.position.z,
            },
            "dimmensions": {
                "width": self.width,
                "height": self.height,
                "depth": self.depth,
            },
            "orientation": {
                "pitch_degrees": self.get_pitch(DEGREES),
                "roll_degrees": self.get_roll(DEGREES),
                "yaw_degrees": self.get_yaw(DEGREES),
                "pitch_radians": self.get_pitch(),
                "roll_radians": self.get_roll(),
                "yaw_radians": self.get_yaw(),
            },
            "orientation_speed": {
                "pitch_speed": self.pitch_speed,
                "roll_speed": self.roll_speed,
                "yaw_speed": self.yaw_speed,
            },
            "integrity": self.integrity,
            "panels": [p.status_report for p in self.panels.values()],
            "reactors": [r.status_report for r in self.reactors],
            "thrusters": [t.status_report for t in self.thrusters],
            "sensors": [t.status_report for t in self.sensors],
            "reaction_wheels": [w.status_report for w in self.reaction_wheels],
            "power_available": self.power_available,
            "power_consumption": self.power_consumption,
            "performance_modifier": self.overall_performance_modifier
        }

    def get_thrusters_by_orientation(self, orientation):
        return [t for t in self.thrusters if t.direction == orientation]

    def apply_acceleration_vectors(self):
        self._apply_thrust()
        self._apply_rotation()
        self.position += self.current_vector

    def get_all_parts(self):
        return {
            part.object_id: part for part in [
                self,
                *self.reactors,
                *self.reaction_wheels,
                *self.panels.values(),
                *self.thrusters,
                *self.sensors,
            ]
        }

    def rotate_vector_by_orientation(self, vector):
        return rotate_vector(
            vector=vector,
            roll=self.get_roll(),
            yaw=self.get_yaw(),
            pitch=self.get_pitch()
        )

    def _apply_rotation(self):
        self._update_rotational_speed()
        self.yaw_degrees += self.yaw_speed
        self.yaw_degrees %= 360
        self.roll_degrees += self.roll_speed
        self.roll_degrees %= 360
        self.pitch_degrees += self.pitch_speed
        self.pitch_degrees %= 360

    def _update_rotational_speed(self):
        for wheel in self.reaction_wheels:
            if wheel.is_active:
                rotational_speed = getattr(self, F"{wheel.axis}_speed")
                rotational_speed += wheel.current_acceleration
                setattr(self, F"{wheel.axis}_speed", rotational_speed)
                wheel.apply_degredation()

    def _apply_thrust(self):
        for thruster in [t for t in self.thrusters]:
            if thruster.is_active:
                self.current_vector += thruster.acceleration_vector
                thruster.apply_degredation()
