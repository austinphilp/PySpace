import sys
from os.path import dirname
sys.path.append("../" + dirname(__file__))

from asyncio import new_event_loop, set_event_loop, start_unix_server
import json
import os
from system import System
from threading import Thread
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
        "reactors": [Reactor(max_output=1000)],
        "reaction_wheels": [
            ReactionWheel(
                axis=axis,
                rotation=directions.CLOCKWISE,
                max_force=750
            )
            for axis in [directions.YAW, directions.ROLL, directions.PITCH]
        ] + [
            ReactionWheel(
                axis=axis,
                rotation=directions.COUNTER_CLOCKWISE,
                max_force=750
            )
            for axis in [directions.YAW, directions.ROLL, directions.PITCH]
        ],
        **{
            F"{direction}_panel": ShipPanel(
                side=directions.COUNTER_DIRECTIONS[direction],
                thrusters=[Thruster(max_force=50.0)],
            ) for direction in directions.DIRECTIONS
        }
    })


class CommandServer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        self._command_server()

    def _command_server(self):
        if os.path.exists("/home/austin/uds_socket"):
            os.remove("/home/austin/uds_socket")
        loop = new_event_loop()
        set_event_loop(loop)
        loop.create_task(start_unix_server(
            self._read_commands_from_socket,
            "/home/austin/uds_socket"
        ))
        loop.run_forever()

    async def _read_commands_from_socket(self, reader, writer):
        request = (await reader.read(256))
        cmd = Command.Parse(request)
        response = cmd.exec(system=system)
        payload = json.dumps(response.value).encode()
        writer.write(
            cmd.command_id.encode().ljust(8, b"\0")
            + str(len(payload)).encode().ljust(8, b"\0")
            + payload
        )
        await writer.drain()
        writer.close()


system = System(ships=[_create_test_ship()])
if __name__ == "__main__":
    i = 0
    thread = CommandServer()
    thread.start()
    while True:
        print("=================== Loop {} ===================".format(i))
        responses = system.perform_tick()
        i += 1
        sleep(0.05)
