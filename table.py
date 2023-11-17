
class Table:
    def __init__(self):
        self.x_minimum = -290
        self.x_maximum = 290
        self.y_minimum = -290
        self.y_maximum = 290

    def collision(self, object):
        if object.pos()[0] > self.x_maximum:
            return True
        elif object.pos()[0] < self.x_minimum:
            return True
        elif object.pos()[1] > self.y_maximum:
            return True
        elif object.pos()[1] < self.y_minimum:
            return True
        else:
            return False
