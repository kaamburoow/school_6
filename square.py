#imports
import turtle

#initializing
screen = turtle.getscreen()
turtle.title("Robot by Mitko Kamburow")
pen = turtle.Turtle()

#start
pen.penup()
pen.pensize(3)
pen.pencolor("#d9c5b2")

#left ear
pen.goto(-172, -4)
pen.pendown()
pen.pencolor("#d9c5b2")
pen.fillcolor("#eed9c4")
pen.begin_fill()
for i in range(8):
    pen.forward(30)
    pen.left(45)
pen.end_fill()
pen.penup()

#right ear
pen.goto(142, -4)
pen.pendown()
pen.begin_fill()
for i in range(8):
    pen.forward(30)
    pen.left(45)
pen.end_fill()
pen.penup()

#head
pen.goto(-50, -125)
pen.pendown()
pen.pencolor("#d9c5b2")
pen.fillcolor("#eed9c4")
pen.begin_fill()
for i in range(8):
    pen.forward(100)
    pen.left(45)
pen.end_fill()
pen.penup()

#left eye
pen.goto(-75, -0)
pen.begin_fill()
pen.pencolor("#ccbaa7")
pen.fillcolor("#6ca580")
pen.pendown()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()
pen.penup()

#right eye
pen.goto(25, 0)
pen.pendown()
pen.begin_fill()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()
pen.penup()

#mouth
pen.goto(-25, -70)
pen.pendown()
pen.pencolor("#ad3e3d")
pen.fillcolor("#8e1e1d")
pen.begin_fill()
for i in range(3):
    pen.forward(50)
    pen.left(120)
pen.end_fill()
pen.penup()

#end
pen.hideturtle()
turtle.done()