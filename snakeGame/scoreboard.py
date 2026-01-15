from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.add()

    def add(self):
        self.score +=1
        print(self.score)
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT,FONT)

    def over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)