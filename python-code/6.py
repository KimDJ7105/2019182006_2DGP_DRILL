import turtle

turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.circle(50)
turtle.write("(200, 200)")

turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.circle(30)
turtle.write("(-200,-200)")

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(50)
turtle.write("home")

turtle.exitonclick();
