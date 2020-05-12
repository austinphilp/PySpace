from space.components.base import PoweredComponent
from space.constants.ratios import KG_PER_MEGAWATT_REACTOR


class Reactor(PoweredComponent):
    def __init__(self, max_output, *args, **kwargs):
        # NOTE: reactor output is measured in MW
        PoweredComponent.__init__(self, *args, **kwargs)
        self.initial_max_output = max_output
        self.mass = max_output * KG_PER_MEGAWATT_REACTOR

    @property
    def current_output(self):
        return self.initial_max_output * self.integrity

    @property
    def status_report(self):
        return {
            **super().status_report,
            "max_output": self.initial_max_output,
            "current_output": self.current_output
        }
