class RobotController:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.is_moving = False

    def start(self):
        self.is_moving = True

    def stop(self):
        self.is_moving = False

    def move(self, dx, dy):
        if self.is_moving:
            self.x += dx
            self.y += dy

    def get_coordinates(self):
        return self.x, self.y

    def update_coordinates(self, dx, dy):
        self.move(dx, dy)