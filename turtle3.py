import turtle

kashyap = turtle.Turtle()

kashyap.color("blue", "cyan")

kashyap.begin_fill()

for i in range(8):
    kashyap.left(135)
    kashyap.forward(200)

kashyap.end_fill()

turtle.done()