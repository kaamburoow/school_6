#imports
import turtle

#welcome message
print("Здравей!")

#inputs
class_number = int(input("Кой номер си в клас? "))

#not_in_range exception
if (class_number < 1 or class_number >= 16):
    print("\033cМоля, въведи число между 1 и 15 включително!")
#find S and P of a triangle 
else:
    #defines
    a = int(class_number)
    h = int(40)
    #main formula
    resultS = str((a*h)/2)
    resultP = str(a*3)
    #output the results
    print("S = " + resultS + " cm².\nP = " + resultP + "cm.")

    #initializing
    screen = turtle.getscreen()
    turtle.title("Triangle by Mitko Kamburow")
    pen = turtle.Turtle()

    #start
    pen.penup()
    pen.pensize(3)
    pen.pencolor("#000000")
    
    #draw that triangle
    pen.pendown()
    pen.fillcolor("#FFE5B4")
    pen.begin_fill()
    for i in range(3):
        pen.forward(a*5)
        pen.left(120)
    pen.end_fill()

    #end
    turtle.done()