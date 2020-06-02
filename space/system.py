from space.utils.misc import CacheMap
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
        self._near_object_map = CacheMap(expiry=50)

    @property
    def bodies(self):
        return self.ships + self.inert_bodies

    def time(self):
        return self.clock.time()

    def perform_tick(self):
        # print("Executing tick")
        for body in self.inert_bodies + self.ships:
            body.apply_acceleration_vectors()
            self._near_object_map[id(body)] = lambda: [
                other for other in (self.inert_bodies + self.ships)
                if get_distance(other.position, body.position) < 200
            ]
            if self.time() % 5 == 0:
                for other_body in self._near_object_map[id(body)]:
                    if other_body is not body and body.is_colliding(other_body):  # noqa
                        print(F"Collision detected between {body} and {other_body}")  # noqa
                        body.perform_collision(other_body)
        self._near_object_map.tick()

    def get_object_by_id(self, object_id):
        for ship in self.ships:
            parts = ship.get_all_parts()
            if object_id in parts:
                return parts[object_id]
        return None

    @property
    def status_report(self):
        return {"ships": [s.status_report for s in self.ships]}
