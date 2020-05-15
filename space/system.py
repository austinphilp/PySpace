class System(object):
    def __init__(self, ships, inert_bodies):
        # TODO(Austin) - Astronomical Body Generation.
        self.ships = ships
        self.inert_bodies = inert_bodies

    @property
    def bodies(self):
        return self.ships + self.inert_bodies

    def perform_tick(self):
        print("Executing tick")
        for body in self.inert_bodies + self.ships:
            body.apply_acceleration_vectors()

    def get_object_by_id(self, object_id):
        for ship in self.ships:
            parts = ship.get_all_parts()
            if object_id in parts:
                return parts[object_id]
        return None

    @property
    def status_report(self):
        return {"ships": [s.status_report for s in self.ships]}
