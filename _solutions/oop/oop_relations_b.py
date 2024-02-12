
class HasPosition:
    current: Point = Point()

    def set_position(self, x, y):
        self.current = Point(x, y)

    def get_position(self):
        return self.current

    def change_position(self, right=0, left=0, up=0, down=0):
        current = self.get_position()
        new_x = current.x + right - left
        new_y = current.y + down - up
        self.set_position(new_x, new_y)
