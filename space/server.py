import socket
from system import System
from time import sleep


from space.command import Command
from space.components import ReactionWheel
from space.components import Reactor
from space.components import Thruster
from space.constants import directions
from space.ship import Ship
from space.ship import ShipPanel


def _create_test_ship():
    return Ship(**{
        directions.YAW: 0,
        directions.ROLL: 0,
        directions.PITCH: 0,
        "reactors": [Reactor(max_output=20)],
        "reaction_wheels": [
            ReactionWheel(
                axis=axis,
                rotation=directions.FORWARD,
                max_force=15
            )
            for axis in [directions.YAW, directions.ROLL, directions.PITCH]
        ],
        **{
            F"{direction}_panel": ShipPanel(
                side=directions.COUNTER_DIRECTIONS[direction],
                thrusters=[Thruster(max_force=10.0)],
            ) for direction in directions.DIRECTIONS
        }
    })


def _read_commands_from_socket():
    commands = []
    with socket.socket() as s:
        s.setblocking(False)
        s.bind(("127.0.0.1", 8000))
        s.listen(200)
        conn, _ = s.accept()
        with conn:
            while True:
                command_payload = conn.recv(256)
                if not command_payload:
                    break
                else:
                    commands.append(Command.Parse(command_payload))
    return commands


if __name__ == "__main__":
    system = System()
    while True:
        system.next_tick(_read_commands_from_socket())
        sleep(0.1)
