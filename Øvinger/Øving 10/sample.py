

class piece:
    def __init__(self, side, type, position):
        self.side = side
        self.live = True
        self.position = (position)
        self.position[0] = position_x
        self.position[1] = position_y