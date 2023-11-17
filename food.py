from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.setposition(x=randint(1-280, 280), y=randint(-280, 280))

    def collision(self, head):
        if self.distance(head) <= 15:
            return True
        else:
            return False

    def replace(self):
        self.setposition(x=randint(-280, 280), y=randint(-280, 280))
