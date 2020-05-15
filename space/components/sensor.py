from math import tan

from vectors import Vector

from space.components.base import PoweredComponent
from space.constants.directions import DIRECTIONAL_VECTORS
from space.constants.math import DEGREES_TO_RADIANS, DEGREES, RADIANS
from space.mixins import OrientationMixin
from space.utils.sanitization import (
    sanitize_sensor_focus,
)
from space.utils.vectors import get_distance, rotate_vector


class Sensor(OrientationMixin, PoweredComponent):
    def __init__(self, base_range, *args, **kwargs):
        super(Sensor, self).__init__(self, *args, **kwargs)
        self.base_range = base_range
        self.focus = sanitize_sensor_focus(kwargs.get('focus', 80))
        # TODO(Austin) - figure out why these aren't inheriting
        self._integrity = 1.0
        self.powered_on = True
        self.attached_panel = kwargs.get('attached_panel')

    @property
    def power_consumption(self):
        return 200

    @property
    def attached_body(self):
        return getattr(self.attached_panel, 'attached_body', None)

    @property
    def range(self):
        return (
            (self.base_range / (self.focus/89))
            * getattr(self.attached_body, 'overall_performance_modifier', 1)
        )

    @property
    def unit_vector(self):
        directional_vector = self.attached_body.rotate_vector_by_orientation(
            rotate_vector(
                vector=DIRECTIONAL_VECTORS[self.attached_panel.side],
                roll=0,
                pitch=(DEGREES_TO_RADIANS*90)-self.get_pitch(),
                yaw=(DEGREES_TO_RADIANS*90)-self.get_yaw()
            )
        )
        return Vector.from_points(self.position, directional_vector).unit()

    @property
    def status_report(self):
        return {
            **super().status_report,
            "focus": self.focus,
            "base_range": self.base_range,
            "current_range": self.range,
            "pitch_degrees": self.get_pitch(DEGREES),
            "yaw_degrees": self.get_yaw(DEGREES),
            "pitch_radians": self.get_pitch(RADIANS),
            "yaw_radians": self.get_yaw(RADIANS),
        }

    def get_sensor_radius_at_point(self, point):
        slope = tan(self.focus * DEGREES_TO_RADIANS)
        return slope * Vector.from_points(self.position, point).magnitude()

    def can_detect(self, body):
        target_distance = min(
            get_distance(body.position, self.position),
            self.range
        )
        # TODO(Austin) - Fix this on the actual library
        # TODO(Austin) - Figure out what the hell the above comment means...
        # I think it has something to do with the wonky way I'm initializing
        # this vector
        x = Vector.from_list((self.position - body.position).to_list())
        dist_along_axis = x.dot(self.unit_vector)
        if 0 <= dist_along_axis <= target_distance:
            cone_radius = self.get_sensor_radius_at_point(
                self.unit_vector.multiply(dist_along_axis)
            )
            orth_distance = (x - self.unit_vector.multiply(
                dist_along_axis)
            ).magnitude()
            return orth_distance < cone_radius and x.magnitude() < self.range
        return False
