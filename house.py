#imports
import turtle

#initialization
screen = turtle.getscreen()
turtle.title("House by Mitko Kamburow")
pen = turtle.Turtle()

#setup
pen.penup()
pen.pensize(3)
pen.pencolor("#000000")
screen.bgcolor("#87CEEB")

#house
pen.goto(-170, 25)
pen.pendown()
pen.fillcolor("#FFE5B4")
pen.begin_fill()
for i in range(4):
    pen.forward(300)
    pen.right(90)
pen.end_fill()

#roof
pen.left(60)
pen.fillcolor("#9D6055")
pen.begin_fill()
for i in range(2):
   pen.forward(300)
   pen.right(120)
pen.end_fill()
pen.penup()

#door
pen.forward(125)
pen.left(90)
pen.forward(300)
pen.left(180)
pen.pendown()
pen.fillcolor("#F2D2BD")
pen.begin_fill()
pen.forward(75)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(75)
pen.end_fill()

#left window
pen.penup()
pen.right(180)
pen.goto(-54, -104)
pen.pendown()
pen.fillcolor("#2B8CC4")
pen.begin_fill()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

#right window
pen.penup()
pen.right(90)
pen.goto(54, -104)
pen.pendown()
pen.begin_fill()
for i in range(4):
    pen.left(90)
    pen.forward(50)
pen.end_fill()

#end
pen.hideturtle()
turtle.done()