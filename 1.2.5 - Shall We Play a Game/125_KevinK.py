import turtle as trtl
import random as rand

#-----SCREEN SETUP-----
wn = trtl.Screen()

wn.setup(width=750, height=600)
wn.cv._rootwindow.resizable(False, False)

#------VARIABLES-----
xcord = -265

letter_list = list('QWERTYUIOPASDFGHJKLZXCVBNM')
current_letter = ''

#-------TURTLES--------
# the turtles for selecting a shape to cut out: the menu screen basically

placeholder_list = []
for s in range(4):
    placeholdercookie = trtl.Turtle(shape='circle')
    placeholdercookie.speed(0)
    placeholdercookie.penup()
    placeholdercookie.turtlesize(8)
    placeholdercookie.color('tan')
    placeholdercookie.goto(xcord, 0)

    xcord += 175
    placeholder_list.append(placeholdercookie)

painter = trtl.Turtle()
painter.penup()
painter.hideturtle()
painter.speed(0)
penS = 5



#----------COOKIE RELATED------------
def draw_circle():
    painter.setheading(0)
    painter.pensize(penS)
    painter.fillcolor('tan')
    painter.pencolor('tan')

    # The cookie part
    painter.goto(-200,-125)
    painter.pendown()
    painter.begin_fill()
    painter.circle(150)
    painter.end_fill()
    painter.penup()

    # The shape part
    painter.pencolor('black')
    painter.goto(-200,-85)
    painter.pendown()
    painter.circle(100)
    painter.penup()

def draw_triangle():
    painter.setheading(0)
    painter.pensize(penS)
    painter.fillcolor('tan')
    painter.pencolor('tan')

    # The cookie part
    painter.goto(-200,-125)
    painter.pendown()
    painter.begin_fill()
    painter.circle(150)
    painter.end_fill()
    painter.penup()

    # The shape part
    painter.pencolor('black')
    painter.goto(-200,-80)
    painter.pendown()
    painter.circle(100,360,3)
    painter.penup()

def draw_star():
    painter.setheading(0)
    painter.pensize(penS)
    painter.fillcolor('tan')
    painter.pencolor('tan')

    # The cookie part
    painter.goto(-200,-125)
    painter.pendown()
    painter.begin_fill()
    painter.circle(150)
    painter.end_fill()
    painter.penup()

    # The shape part
    painter.pencolor('black')
    painter.goto(-200,-80)
    painter.pendown()
    painter.circle(100,360,6)
    painter.penup()

def draw_umbrella():
    painter.setheading(0)
    painter.pensize(penS)
    painter.fillcolor('tan')
    painter.pencolor('tan')

    # The cookie part
    painter.goto(-200,-125)
    painter.pendown()
    painter.begin_fill()
    painter.circle(150)
    painter.end_fill()
    painter.penup()

    # The shape part
    painter.pencolor('black')
    painter.goto(-200,-80)
    painter.pendown()
    painter.circle(100,180)
    painter.penup()



#-------FUNCTIONS-------
def select_shape(x,y):
    global starting
    cookieselection = rand.randint(1,4)
    starting = False
    
    return cookieselection

def draw_shape(num):
    # The number that'll set how many letters are to be pressed for each shape: removing any letters after the number
    cap = 0
    if num == 1:
        draw_triangle()
        cap = 10
    elif num == 2:
        draw_circle()
        cap = 15
    elif num == 3:
        draw_star()
        cap = 20
    elif num == 4:
        draw_umbrella()
        cap = 0
    
    list_cap(cap)

def list_cap(listlength):
    while len(letter_list) not in range(listlength):
        index = 0
        letter_list.pop(index)

        index += 1
        print(letter_list)

    
    



# TODO 6: Have letters show up next to the cookie, that will change like in apple avalanche

# TODO 7: Timer

# TODO 8: Point system, removing a point whenever a wrong key is pressed/adding a point whenever a right key is pressed



#----------GAME-----------

# Pauses the program from continuing and assigning a value to 'userselection'
starting = True # Variable is set to false in the select_shape function

while starting:
    placeholder_list[0].onclick(select_shape)
    placeholder_list[1].onclick(select_shape)
    placeholder_list[2].onclick(select_shape)
    placeholder_list[3].onclick(select_shape)

# After exiting the while loop, the userselection variable is assigned a variable based on the return from the function
userselection = select_shape(0,0)

for d in placeholder_list:
    d.hideturtle()
    
draw_shape(userselection)
list_cap(userselection) # Giving the parameter the value of userselection




#--------SCREEN--------
# TODO 9: Win screen, showing the cookie being cracked? Displaying points and name










wn.mainloop()
















# TODO OPTIONAL (10): Turtle tracing the shape of the cookie as keys are being pressed (OPTIONAL)

# TODO 11: Leaderboard (Create a txt file)

# TODO 12: Animation of revealing the inital selection of the cookie