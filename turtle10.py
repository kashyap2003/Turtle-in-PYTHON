import turtle

kashyap = turtle.Turtle()
kashyap.getscreen().bgcolor("cyan")
kashyap.speed(10)

kashyap.penup()
kashyap.goto((-250, 100))
kashyap.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)

star(kashyap, 360)

turtle.done()