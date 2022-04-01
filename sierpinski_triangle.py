import turtle
import random

turtle.setup(600, 600)
wn = turtle.Screen()
turtle.colormode(255)

pen = turtle.Turtle()
pen.penup()
pen.left(60)
pen.speed(0)
pen.pensize(0)
pen.goto(wn.window_width()/3, wn.window_height()/3)

turtle.tracer(0, 0)
points = []

for i in range(3):
    pen.left(120)
    pen.forward(400)
    x = pen.xcor()
    y = pen.ycor()
    points.append((x, y))
    pen.dot()

randomPoint = random.randint(0, 2)
x, y = points[randomPoint]
pen.goto(x, y)
lastPoint = (0, 0)
newPoint = ((points[randomPoint][0] + lastPoint[0])/2, (points[randomPoint][1] + lastPoint[1])/2)

for i in range(5000):
    r = random.randint(3, 4)
    g = random.randint(94, 255)
    b = random.randint(28, 70)
    pen.pencolor((r, g, b))

    randomPoint = random.randint(0, 2)
    newPoint = ((points[randomPoint][0] + lastPoint[0])/2, (points[randomPoint][1] + lastPoint[1])/2)
    lastPoint = newPoint
    pen.goto(newPoint)
    pen.dot()

turtle.update()
turtle.exitonclick()
