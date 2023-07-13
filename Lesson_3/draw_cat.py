from turtle import *

my_cat = Turtle()
my_cat.speed(3)
my_cat.screen.setup(1200, 800)
my_cat.screen.bgcolor('pink')
my_cat.shape("circle")
my_cat.pensize('12')

def movePen(my_cat, x, y): #переместить на точку x, y
    my_cat.up()
    my_cat.setposition(x, y)
    my_cat.down()

def movePenX(my_cat, x):
    my_cat.up()
    my_cat.setx(x)
    my_cat.down()

def movePenY(my_cat, y):
    my_cat.up()
    my_cat.sety(y)
    my_cat.down()

#Голова
movePenY(my_cat, -320)
my_cat.circle(300)

#Глаза
eyeSpaceX = 60
eyePosY = 60
eyeRad = 60

#Правый
movePen(my_cat, eyeSpaceX, eyePosY)
my_cat.right(90)
my_cat.circle(eyeRad, -180)

#Левый
movePen(my_cat, -eyeSpaceX, eyePosY)
my_cat.circle(eyeRad, 180)



my_cat.screen.exitonclick()
my_cat.screen.mainloop()
