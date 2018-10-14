from vectors import Vector


CLOCKWISE = "CW"
COUNTER_CLOCKWISE = "CCW"

STARBOARD = "starboard"
PORT = "port"
FORWARD = "forward"
AFT = "aft"
OVERHEAD = "overhead"
DECK = "deck"

DIRECTIONS = [STARBOARD, PORT, FORWARD, AFT, OVERHEAD, DECK]

COUNTER_DIRECTIONS = {
    STARBOARD: PORT,
    PORT: STARBOARD,
    FORWARD: AFT,
    AFT: FORWARD,
    OVERHEAD: DECK,
    DECK: OVERHEAD,
}

DIRECTIONAL_VECTORS = {
    STARBOARD: Vector(0, 1, 0),
    PORT: Vector(0, -1, 0),
    FORWARD: Vector(1, 0, 0),
    AFT: Vector(-1, 0, 0),
    OVERHEAD: Vector(0, 0, 1),
    DECK: Vector(0, 0, -1),
}

PITCH = "pitch"
ROLL = "roll"
YAW = "yaw"
