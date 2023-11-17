from turtle import Turtle


class Snake:
    snake = []

    def __init__(self):
        for i in range(0, 3):
            temp = Turtle()
            temp.shape("square")
            temp.color("green")
            temp.penup()
            temp.shapesize(1, 1)
            x = [0, -20, -40, -60, -80, -100, -120, -140, -160, -180]
            temp.setposition(x=x[i], y=0)
            self.snake.append(temp)

    def up(self):

        if self.snake[0].heading() != -90:
            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i].setposition(x=self.snake[i - 1].pos()[0], y=self.snake[i - 1].pos()[1])
            self.snake[0].setheading(90)
            self.snake[0].forward(20)

    def down(self):

        if self.snake[0].heading() != 90:
            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i].setposition(x=self.snake[i - 1].pos()[0], y=self.snake[i - 1].pos()[1])
            self.snake[0].setheading(-90)
            self.snake[0].forward(20)

    def reset(self):
        for i in self.snake:
            i.goto(1000,1000)
        self.snake.clear()
        self.__init__()
    def right(self):

        if self.snake[0].heading() != 180:
            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i].setposition(x=self.snake[i - 1].pos()[0], y=self.snake[i - 1].pos()[1])
            self.snake[0].setheading(0)
            self.snake[0].forward(20)

    def left(self):

        if self.snake[0].heading() != 0:
            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i].setposition(x=self.snake[i - 1].pos()[0], y=self.snake[i - 1].pos()[1])
            self.snake[0].setheading(180)
            self.snake[0].forward(20)

    def add(self):
        temp = Turtle()
        temp.shape("square")
        temp.color("green")
        temp.penup()
        temp.shapesize(1, 1)
        self.snake.append(temp)

    def collision(self):
        for i in range(1, len(self.snake)):
            if self.snake[0].distance(self.snake[i]) < 10:
                return True

    def get_snake(self):
        return self.snake
