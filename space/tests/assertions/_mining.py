from space.asteroid import Asteroid
from space.components import Reactor, MiningLaser
from space.ship import ShipPanel, Ship


def _get_mining_lasers_for_assertion(mining_range, mining_rate, has_power):
    reactor = Reactor(max_output=200)
    ship = Ship(
        forward_panel=ShipPanel(
            side="forward",
            mining_lasers=MiningLaser(
                base_range=mining_range,
                mining_rate=mining_rate
            )
        ),
        reactors=[reactor] if has_power else []
    )
    return [
        laser for panel in ship.panels.values()
        for laser in panel.mining_lasers
    ]


def _assert_can_set_target(target_pos, target_mass, *args, **kwargs):
    if kwargs.pop('test', False):
        import pdb; pdb.set_trace()  # noqa
    target = Asteroid(position=target_pos, mass=target_mass)
    laser = _get_mining_lasers_for_assertion(*args, **kwargs)[0]
    laser.set_target(target)
    if kwargs.get('expect_failure'):
        assert laser._target is None
    else:
        assert laser._target is not None


def _assert_can_mine(target_pos, target_mass, *args, **kwargs):
    if kwargs.pop('test', False):
        import pdb; pdb.set_trace()  # noqa
    target = Asteroid(position=target_pos, mass=target_mass)
    laser = _get_mining_lasers_for_assertion(*args, **kwargs)[0]
    laser.set_target(target)
    laser.perform_tick(target)
    old_mass = target.mass
    assert old_mass == old_mass - laser.mining_rate
    assert laser.attached_body.storage == laser.mining_rate
