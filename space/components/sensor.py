from math import tan

from mathutils.geometry import intersect_point_line
from vectors import Vector

from space.components.base import PoweredComponent
from space.constants.directions import DIRECTIONAL_VECTORS
from space.constants.math import DEGREES_TO_RADIANS
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

    @property
    def power_consumption(self):
        return 200

    @property
    def attached_body(self):
        return self.attached_panel.attached_body

    @property
    def range(self):
        return (
            self.base_range *
            self.focus/9 *
            self.attached_body.overall_performance_modifier
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

    def get_sensor_radius_at_point(self, point):
        slope = tan(self.focus * DEGREES_TO_RADIANS)
        return slope * Vector.from_points(self.position, point).magnitude()

    def can_detect(self, body):
        target_distance = min(
            get_distance(body.position, self.position),
            self.range
        )
        sensor_vector = self.unit_vector.multiply(target_distance)
        intersection_point, intersect_distance = intersect_point_line(
            body.position.to_list(),
            self.position.to_list(),
            sensor_vector.to_list()
        )
        intersection_point = Vector(*intersection_point)
        intersect_distance = get_distance(sensor_vector, intersection_point)
        sensor_radius = self.get_sensor_radius_at_point(intersection_point)
        return intersect_distance <= sensor_radius
