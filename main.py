
from turtle import Screen
import time
from ssnake import Snake
from food import Food
from scoreboard import Scoreboard
from table import Table

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()

table = Table()
screen.listen()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    if food.collision(snake.get_snake()[0]):
        food.replace()
        snake.add()
        scoreboard.plus()
    if table.collision(snake.get_snake()[0]) or snake.collision():
        scoreboard.reset()
        snake.reset()
    for i in range(len(snake.snake)-1, -1, -1):
        if i == 0:
            snake.get_snake()[i].forward(20)
        else:
            snake.get_snake()[i].setposition(x=snake.get_snake()[i-1].pos()[0], y=snake.get_snake()[i-1].pos()[1])
        screen.onkey(snake.up, "w")
        screen.onkey(snake.down, "s")
        screen.onkey(snake.right, "d")
        screen.onkey(snake.left, "a")

    with open("highscore.txt" , "w") as file:
        file.write(str(scoreboard.highscore))


screen.exitonclick()
