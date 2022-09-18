import turtle

shape = input("Enter shape : ")

if shape == 'circle' :
    turtle.reset()
    turtle.circle(50)
elif shape == 'triangle' :
    turtle.reset()
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
else :
    print("Unknown shape")

turtle.exitonclick()