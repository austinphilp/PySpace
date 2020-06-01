from space.utils.vectors import get_distance


class System(object):
    def __init__(self, ships, inert_bodies):
        # TODO(Austin) - Astronomical Body Generation.
        self.ships = ships
        for ship in self.ships:
            ship.system = self
        self.inert_bodies = inert_bodies
        for body in self.inert_bodies:
            body.system = self

    @property
    def bodies(self):
        return self.ships + self.inert_bodies

    def time(self):
        return self.clock.time()

    def perform_tick(self):
        # print("Executing tick")
        for body in self.inert_bodies + self.ships:
            body.apply_acceleration_vectors()
            near_bodies = [
                other for other in (self.inert_bodies + self.ships)
                if get_distance(other, body) < 200
            ]
            for other_body in near_bodies:
                body.is_colliding(other_body)
                body.perform_collision(other_body)

    def get_object_by_id(self, object_id):
        for ship in self.ships:
            parts = ship.get_all_parts()
            if object_id in parts:
                return parts[object_id]
        return None

    @property
    def status_report(self):
        return {"ships": [s.status_report for s in self.ships]}
