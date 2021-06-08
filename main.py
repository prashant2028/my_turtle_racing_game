from turtle import Turtle, Screen
import random
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle_racing_game")
screen.tracer(0)
directions = [(-280, -260), (-280, -150), (-280, 0), (-280, 150), (-280, 260)]
turtles = []
colors = ["red", "blue", "yellow", "green", "black"]

for position in range(0, 5):
    tim = Turtle("turtle")
    tim.penup()
    tim.color(colors[position])
    tim.goto(directions[position])
    turtles.append(tim)


game = True
while game:
    screen.update()
    time.sleep(0.1)
    for each_turtle in turtles:

        each_turtle.forward(random.randint(1, 15))
        if each_turtle.xcor() > 270:
            each_turtle.setheading(180)

        elif each_turtle.xcor() < -280:
            game = False
            winner_color = each_turtle.pencolor()
            print(f"The winner is {winner_color} turtle")



screen.exitonclick()