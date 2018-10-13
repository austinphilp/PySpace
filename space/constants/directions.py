from vectors import Vector
STARBOARD = "dir_sb"
PORT = "dir_port"
FORWARD = "dir_fore"
AFT = "dir_aft"
OVERHEAD = "dir_ovrhead"
DECK = "dir_deck"

DIRECTIONAL_VECTORS = {
    STARBOARD: Vector.from_list(0, 1, 0),
    PORT: (0, -1, 0),
    FORWARD: (1, 0, 0),
    AFT: (-1, 0, 0),
    OVERHEAD: (0, 0, 1),
    DECK: (0, 0, -1),
}

PITCH = "pitch"
ROLL = "roll"
YAW = "yaw"
