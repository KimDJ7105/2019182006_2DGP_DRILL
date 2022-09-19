import turtle
import random

def drungken() :
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(100,200))
    turtle.stamp()

def restart() :
    turtle.reset()

turtle.shape("turtle")

turtle.onkey(drungken, ' ')
turtle.onkey(restart, 'Escape')
turtle.listen()

turtle.exitonclick()
