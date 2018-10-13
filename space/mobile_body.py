from body import Body


class MobileBody(Body):
    def roll(self, acceleration):
        self.roll_speed += acceleration

    def yaw(self, acceleration):
        self.yaw_speed += acceleration

    def pitch(self, acceleration):
        self.pitch_speed += acceleration
