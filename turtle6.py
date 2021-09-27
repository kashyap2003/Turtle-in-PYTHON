import turtle
import math

kashyap = turtle.Turtle()

kashyap.speed(10)

kashyap.color("red", "yellow")

kashyap.begin_fill()

for i in range(92):
    kashyap.forward(math.sqrt(i)*10)
    kashyap.left(i%90)

kashyap.end_fill()

turtle.done()