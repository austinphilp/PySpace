from space.components.base import PoweredComponent


class Reactor(PoweredComponent):
    def __init__(self, max_output, *args, **kwargs):
        # NOTE: reactor output is measured in MW
        PoweredComponent.__init__(self, *args, **kwargs)
        self.initial_max_output = max_output

    def current_output(self):
        return self.initial_max_output * self.integrity
