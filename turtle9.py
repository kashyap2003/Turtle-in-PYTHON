import turtle

kashyap = turtle.Turtle()
kashyap.getscreen().bgcolor("cyan")

def star(turtle, size):
    for i in range(5):
        turtle.forward(size)
        turtle.left(216)

star(kashyap, 100)

turtle.done()