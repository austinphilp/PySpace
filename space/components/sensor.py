from math import tan
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
        return 20

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
    def directional_vector(self):
        return rotate_vector(
            vector=DIRECTIONAL_VECTORS[self.attached_panel.side],
            roll=0,
            pitch=90-self.get_pitch(),
            yaw=90-self.get_yaw()
        )

    def get_sensor_radius_by_distance(self, distance):
        slope = tan(self.focus * DEGREES_TO_RADIANS)
        return slope * distance

    def can_detect(self, body):
        # if self.focus == 5:
        #     import pdb; pdb.set_trace()

        distance = min(get_distance(
            body.position,
            self.attached_panel.ship.position
        ), self.range)
        sensor_vector = self.directional_vector.multiply(distance)
        radius = self.get_sensor_radius_by_distance(distance)
        return get_distance(sensor_vector, body.position) <= radius
