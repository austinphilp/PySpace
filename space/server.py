from asyncio import new_event_loop, set_event_loop, start_unix_server
import json
import os
from random import normalvariate, uniform, choice
from system import System
from threading import Thread
from time import sleep
import sys
from os.path import dirname

sys.path.append("../" + dirname(__file__))

from vectors import Point, Vector

from space.command import Command
from space.components import ReactionWheel, Reactor, Sensor, Thruster
from space.constants import directions
from space.ship import Ship, ShipPanel
from space.asteroid import Asteroid


def _create_random_position(avoid_center=True):
    return Point(
        *[
            uniform((100 if avoid_center else 0), 10000) * choice([-1, 1])
            for _ in range(3)
        ]
    )


def _create_random_vector():
    return Vector(*[uniform(-0.1, 0.1) for _ in range(3)])


def _create_asteroids():
    return [
        Asteroid(
            position=_create_random_position(),
            vector=_create_random_vector(),
            mass=max(normalvariate(10000, 2500), 2500),
            yaw_speed=normalvariate(0.0, 0.05),
            pitch_speed=normalvariate(0.0, 0.05),
            roll_speed=normalvariate(0.0, 0.05),
        ) for _ in range(int(normalvariate(500, 100)))
    ]


def _create_test_ship():
    return Ship(**{
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
                sensors=[Sensor(base_range=500.0, focus=90)],
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


system = System(ships=[_create_test_ship()], inert_bodies=_create_asteroids())
if __name__ == "__main__":
    i = 0
    thread = CommandServer()
    thread.start()
    while True:
        print("=================== Loop {} ===================".format(i))
        responses = system.perform_tick()
        i += 1
        sleep(1.05)
