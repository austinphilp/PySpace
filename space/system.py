class System(object):
    def __init__(self, ships):
        # TODO(Austin) - Astronomical Body Generation.
        self.ships = ships

    def perform_tick(self, commands):
        for command in commands:
            command.exec(system=self)
        for ship in self.ships:
            ship.apply_accelleration_vector()

    def report(self):
        report = {"ship_reports": [s.status_report for s in self.ships]}
        return report
