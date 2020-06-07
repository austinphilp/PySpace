from vectors import Point
from space.tests.assertions import _assert_can_mine, _assert_can_set_target


def test_can_set_target():
    _assert_can_set_target(
        target_pos=Point(100, 0, 0),
        target_mass=100,
        mining_range=500,
        mining_rate=1,
        has_power=True
    )


def test_cannot_set_target_out_of_range():
    _assert_can_set_target(
        target_pos=Point(500, 0, 0),
        target_mass=100,
        mining_range=100,
        mining_rate=1,
        has_power=True,
        expect_failure=True
    )


def test_cannot_set_target_no_mass():
    _assert_can_set_target(
        target_pos=Point(500, 0, 0),
        target_mass=0,
        mining_range=100,
        mining_rate=1,
        has_power=True,
        expect_failure=True
    )


def test_can_mine_chunk():
    _assert_can_mine(
        target_pos=Point(100, 0, 0),
        target_mass=100,
        mining_range=500,
        mining_rate=1,
        has_power=True,
    )


def test_cannot_mine_out_of_range():
    _assert_can_mine(
        target_pos=Point(500, 0, 0),
        target_mass=100,
        mining_range=100,
        mining_rate=1,
        has_power=True,
        expect_failure=True
    )


def test_cannot_mine_no_power():
    _assert_can_mine(
        target_pos=Point(500, 0, 0),
        target_mass=100,
        mining_range=100,
        mining_rate=1,
        has_power=False,
        expect_failure=True
    )
