class System(object):
    def __init__(self, ships):
        # TODO(Austin) - Astronomical Body Generation.
        self.ships = ships

    def perform_tick(self, commands):
        for command in commands:
            command.exec(system=self)
        for ship in self.ships:
            ship.apply_accelleration_vector()

    def get_object_by_id(self, object_id):
        for ship in self.ships:
            parts = ship.get_all_parts()
            if object_id in parts:
                return parts[object_id]
        return None

    @property
    def status_report(self):
        return {"ships": [s.status_report for s in self.ships]}
