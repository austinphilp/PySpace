import json
import os
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
    s.listen(200)
    try:
        conn, _ = s.accept()
    except BlockingIOError:
        return [], []
    conn.setblocking(False)
    while conn:
        connections.append(conn)
        try:
            command_payload = conn.recv(256)
        except BlockingIOError:
            break
        if not command_payload:
            break
        else:
            cmd = Command.Parse(command_payload, connection=conn)
            commands.append(cmd)
    return commands, connections


if __name__ == "__main__":
    system = System(ships=[_create_test_ship()])
    i = 0
    if os.path.exists("/home/austin/uds_socket"):
        os.remove("/home/austin/uds_socket")
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.setblocking(False)
        s.bind("/home/austin/uds_socket")
        while True:
            print("=================== Loop {} ===================".format(i))
            print("Reading new commands form sockets")
            commands, connections = _read_commands_from_socket(s)
            print("Executing tick")
            responses = system.perform_tick(commands)
            print("sending responses")
            for response in responses:
                payload = json.dumps(response.value).encode()
                response.connection.send(
                    response.command_id.encode().ljust(8, b"\0")
                    + str(len(payload)).encode().ljust(8, b"\0")
                    + payload
                )
            for conn in connections:
                conn.close()
            print("closed all connections")
            i += 1
            sleep(0.1)
