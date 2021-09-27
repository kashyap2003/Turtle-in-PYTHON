import turtle
import math

kashyap = turtle.Turtle()

kashyap.speed(10)

kashyap.color("red", "yellow")

kashyap.begin_fill()

for i in range(700):
    kashyap.forward(10)
    kashyap.left(math.sin(i/10)*25)
    kashyap.left(20)

kashyap.end_fill()

turtle.done()