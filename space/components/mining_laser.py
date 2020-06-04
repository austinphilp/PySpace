from space.components.base import PoweredComponent
from space.utils.vectors import get_distance


class MiningLaser(PoweredComponent):
    def __init__(self, base_range, mine_rate, *args, **kwargs):
        super(MiningLaser, self).__init__(self, *args, **kwargs)
        self.base_range = base_range
        self.mine_rate = mine_rate
        # TODO(Austin) - figure out why these aren't inheriting
        self._integrity = 1.0
        self.powered_on = True
        self.attached_panel = kwargs.get('attached_panel')
        self._target = None

    @property
    def power_consumption(self):
        if self.current_target and self.powered_on:
            return self.base_range * self.mine_rate
        else:
            return 0

    @property
    def attached_body(self):
        return getattr(self.attached_panel, 'attached_body', None)

    @property
    def range(self):
        return (
            self.base_range
            * getattr(self.attached_body, 'overall_performance_modifier', 1)
        )

    @property
    def status_report(self):
        return {
            **super().status_report,
            "base_range": self.base_range,
            "current_range": self.range,
            "mine_rate": self.mine_rate,
            "target_object": self.current_target,
        }

    @property
    def current_target(self):
        if self._target is None:
            return
        # TODO(Austin) - optimize so this distance calculation is only ran once
        # per tick
        target_dist = get_distance(
            self._target.position,
            self.attached_body.position
        )
        if target_dist > self.current_range or self._target.mass <= 0:
            self.clear_target()
        return self._target

    def clear_target(self):
        self._target = None

    def set_target(self, target):
        target_dist = get_distance(
            self._target.position,
            self.attached_body.position
        )
        if target_dist < self.current_range and self._target.mass > 0:
            self._target = target

    def perform_tick(self):
        target = self.current_target
        if target is not None:
            target.mass -= self.mine_rate
            if target.mass <= 0:
                self.clear_target()
            # TODO(Austin) - Add capacity to storage
            self.attached_body.storage += self.mine_rate
