from decimal import Decimal
from decimal import ROUND_HALF_UP
from vectors import Vector


def apply_acceleration_to_vector(self, vector, acceleration):
    return Vector.from_list([x * self.current_acceleration for x in vector])


def round_point(point):
    point.x = point.x.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
    point.y = point.y.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
    point.z = point.z.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
    return point
