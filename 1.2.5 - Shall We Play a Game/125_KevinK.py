import turtle as trtl
import random as rand

#------VARIABLES-----
xcord = -265

#-------TURTLES--------
# the turtles for selecting a shape to cut out: starting the game basically
for s in range(4):
    shapeselection = trtl.Turtle(shape='circle')
    shapeselection.speed(0)
    shapeselection.penup()
    shapeselection.turtlesize(8)
    shapeselection.color('tan')
    shapeselection.goto(xcord, 0)

    xcord += 175

painter = trtl.Turtle()
painter.penup()
painter.hideturtle()
painter.speed(0)
penS = 5

#----------COOKIE RELATED------------
def draw_circle():
    painter.pensize(penS)
    painter.fillcolor('tan')
    painter.pencolor('tan')

    # The cookie part
    painter.goto(-200,-125)
    painter.pendown()
    painter.begin_fill()
    painter.circle(150)
    painter.end_fill()
    painter.penup

    # The shape part
    painter.pencolor('black')
    painter.goto(-200,-100)
    painter.pensize(1)
    painter.circle(75)

# TODO 2: Functions to draw out the 4 cookies
# TODO 2.1: List storing these functions


#-------FUNCTIONS-------
def select_shape(x,y):
    print('nvdjs zcx')

# TODO 3: From todo 1, create a function that'll randomly generate a number
# TODO 3.1: return a number from the function based on the cookie selected

# TODO 4: List of letters 'list()' that cap out based on the number from todo 3.1

# TODO 6: Have letters show up next to the cookie, that will change like in apple avalanche

# TODO 7: Timer

# TODO 8: Point system, removing a point whenever a wrong key is pressed/adding a point whenever a right key is pressed



#----------GAME-----------
# TODO 5: Display the shape of the cookie

draw_circle()
shapeselection.onclick(select_shape)



#--------SCREEN--------
# TODO 9: Win screen, showing the cookie being cracked? Displaying points and name








wn = trtl.Screen()

wn.setup(width=750, height=600)
wn.cv._rootwindow.resizable(False, False)

wn.mainloop()
















# TODO OPTIONAL (10): Turtle tracing the shape of the cookie as keys are being pressed (OPTIONAL)

# TODO 11: Leaderboard (Create a txt file)

# TODO 12: Animation of revealing the inital selection of the cookie