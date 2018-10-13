from decimal import Decimal


def enforce_range(val, min_val, max_val):
    return max(min(val, max_val), min_val)


def sanitize_integrity(integrity):
    return enforce_range(integrity, Decimal('0.0'), Decimal('1.0'))


def sanitize_throttle(throttle):
    return enforce_range(throttle, Decimal('0.0'), Decimal('1.2'))
