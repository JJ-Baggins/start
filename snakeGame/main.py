from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect food collision
    if snake.head.distance(food) <15:
        print("nom nom nom")
        food.move()
        snake.extend()
        board.add()

    #Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameOn = False
        board.over()

    #Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameOn = False
            board.over()
























screen.exitonclick()