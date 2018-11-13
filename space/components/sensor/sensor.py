from math import tan
from space.components import PoweredComponent
from space.constants.directions import DIRECTIONAL_VECTORS
from space.constants.math import DEGREES_TO_RADIANS
from space.utils.sanitization import (
    sanitize_sensor_focus,
    sanitize_sensor_orientation
)
from space.utils.vectors import get_distance, rotate_vector


class Sensor(PoweredComponent):
    def __init__(self, base_range, *args, **kwargs):
        PoweredComponent.__init__(self, *args, **kwargs)
        self.base_range = base_range
        self.focus = sanitize_sensor_focus(kwargs.get('focus', 89))
        self.pitch_degrees = sanitize_sensor_orientation(kwargs.get('pitch'))
        self.yaw_degrees = sanitize_sensor_orientation(kwargs.get('yaw'))

    @property
    def range(self):
        return self.base_range * self.focus/9

    @property
    def _directional_vector(self):
        return rotate_vector(
            vector=DIRECTIONAL_VECTORS[self.attached_panel.side],
            roll=0,
            pitch=self.get_pitch(),
            yaw=self.get_yaw()
        )

    def get_sensor_radius_by_distance(self, distance):
        slope = tan(self.focus * DEGREES_TO_RADIANS)
        return slope * distance

    def can_detect(self, body):
        distance = get_distance(self.attached_panel.ship.position)
        sensor_vector = self.directional_vector.multiply(distance)
        radius = self.get_sensor_radius_by_distance(distance)
        return get_distance(sensor_vector, body) <= radius
