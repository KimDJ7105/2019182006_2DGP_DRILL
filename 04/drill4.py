import turtle

count = 6
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()

while (count > 0) :
    turtle.forward(500)
    turtle.backward(500)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    count = count - 1


count = 6
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()

turtle.left(90)

while (count > 0) :
    turtle.forward(500)
    turtle.backward(500)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    count = count - 1


turtle.exitonclick()