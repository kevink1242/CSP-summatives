import turtle as trtl
import random as rand

#-----SCREEN SETUP-----
wn = trtl.Screen()

wn.setup(width=750, height=600)
wn.cv._rootwindow.resizable(False, False)

#------VARIABLES-----
xcord = -265

original_letter_list = list('qwertyuiopasdfghjklzxcvbnm')

updated_letter_list = list()

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

cookie_list = [draw_triangle, draw_circle, draw_star, draw_umbrella]


#-------FUNCTIONS-------
def select_shape(x,y):
    global starting
    cookieselection = rand.randint(0,len(cookie_list)-1)
    starting = False
    
    return cookieselection


player_name = player_name[:max_char]
def list_cap(cookienum):
    # Different levels of difficulty based on the integer of cookienum (userselection)
    cap = 0
    listlength = len(original_letter_list)
    if cookienum == 0:
        cap = 6
    elif cookienum == 1:
        cap = 
    else:
        cap = 0

    
    



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
print('userselection variable: ',userselection)

for d in placeholder_list:
    d.hideturtle()
    
# Drawing the shape
if userselection == 0:
    draw_triangle()
    print('drawn circle')
elif userselection == 1:
    draw_circle()
    print('drawn triangle')
elif userselection == 2:
    draw_star()
    print('drawn star')
elif userselection == 3:
    draw_umbrella()
    print('drawn umbrella')
list_cap(userselection) # Giving the parameter the value of userselection




#--------SCREEN--------
# TODO 9: Win screen, showing the cookie being cracked? Displaying points and name










wn.mainloop()
















# TODO OPTIONAL (10): Turtle tracing the shape of the cookie as keys are being pressed (OPTIONAL)

# TODO 11: Leaderboard (Create a txt file)

# TODO 12: Animation of revealing the inital selection of the cookie