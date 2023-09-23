from turtle import *


#we want to paint a house

speed(10)
#step1: draw a square
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#draw a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("purple")
begin_fill()
begin_fill()
left(30)
forward(60)
left(90)
forward(50)
left(90)
forward(55)
end_fill()

right(90)

forward(100)
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(55)
end_fill()



exitonclick()