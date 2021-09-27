import turtle

kashyap = turtle.Turtle()

kashyap.speed(10)

kashyap.color("red", "yellow")

kashyap.begin_fill()

for i in range(36):
    kashyap.left(170)
    kashyap.forward(200)

kashyap.end_fill()

turtle.done()