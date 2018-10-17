
def enforce_range(val, min_val, max_val):
    return max(min(val, max_val), min_val)


def sanitize_integrity(integrity):
    return enforce_range(integrity, 0.0, 1.0)


def sanitize_throttle(throttle):
    return enforce_range(throttle, 0.0, 1.2)
