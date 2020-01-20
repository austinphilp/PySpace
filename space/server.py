import json
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


def _read_commands_from_socket(s):
    commands = []
    connections = []
    s.setblocking(False)
    s.bind(("127.0.0.1", 8000))
    s.listen(200)
    conn, _ = s.accept()
    while conn:
        connections.append(conn)
        while True:
            command_payload = conn.recv(256)
            if not command_payload:
                break
            else:
                cmd = Command.Parse(command_payload)
                commands.append(cmd)
    return commands, connections


if __name__ == "__main__":
    system = System()
    while True:
        print("Entering new game loop")
        with socket.socket() as s:
            print("Reading new commands form sockets")
            commands, connections = _read_commands_from_socket(s)
            print("Executing tick")
            system.next_tick(commands)
            print("sending status reports")
            for connection in connections:
                connection.send(json.dumps(system.status_report).encode())
                connection.close()
            print("closed all connections")
        sleep(1)
