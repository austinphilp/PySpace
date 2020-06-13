from space.components.base import PoweredComponent


class Factory(PoweredComponent):
    def __init__(self, build_rate, *args, **kwargs):
        super(Factory, self).__init__(self, *args, **kwargs)
        self.build_rate = build_rate
        self.storage = 0
        # TODO(Austin) - figure out why these aren't inheriting
        self._integrity = 1.0
        self.powered_on = True
        self.attached_panel = kwargs.get('attached_panel')
        self._attached_body = kwargs.get('attached_body')
        self.build_queue = []
        self.current_progress = 0

    @property
    def power_consumption(self):
        if self.current_target and self.powered_on:
            return self.base_range * self.mine_rate
        else:
            return 0

    @property
    def attached_body(self):
        return self._attached_body or getattr(
            self.attached_panel,
            'attached_body',
            None
        )

    @property
    def status_report(self):
        return {
            **super().status_report,
            "build_queue": self.build_queue,
            "build_rate": self.build_rate,
            "current_progress": self.current_progress,
        }

    def deposit(self, source, amount):
        if amount > source.storage:
            amount = source.storage
        self.storage += amount
        source.storage -= amount

    def withdraw(self, destination, amount):
        if amount > self.storage:
            amount = self.storage
        self.storage -= amount
        destination.storage += amount

    def perform_tick(self):
        # system = self.attached_body.system
        if len(self.build_queue) > 0:
            if self.current_progress >= 1:
                self.current_progress = 0
                return self.buildQueue.pop().build(self.attached_body.system)
            else:
                self.current_progress += self.build_rate
