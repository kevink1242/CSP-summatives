import turtle as trtl
import random as rand

#-----SCREEN SETUP-----
wn = trtl.Screen()

wn.setup(width=750, height=600)
wn.cv._rootwindow.resizable(False, False)

wn.listen()

#------VARIABLES-----
xcord = -265

#letter_list = list('QWERTYUIOPASDFGHJKLZXCVBNMWERTYUIOPASDFGHJKLZXCVBQWERTYUIOPASDFGHJKLZXCVBNMWERTYUIOPASDFGHJKLZXCNMEE') # = 100 letters
letter_list = list('QWERTYUIOPASDFGHJKLZXCVBNMWERTYUIOPASDFGHJKLZXCVBQWERTYUIOPASDFGHJKLZXCVBNMWERTYUIOPASDFGH') # = 90 letters
currentletter = 'E'

lives = 3

# Timer
totaltime = 50
counter_interval = 1000


gamefin = False # Variable for if the game is finished
# Essentially only purpose is for the timer. Fixed the issue of the timer counting down even after finishing the game



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

# For the actual game part of the program 
keysignifier = trtl.Turtle(shape='circle')
keysignifier.hideturtle()
keysignifier.penup()
keysignifier.color('lightgray')
keysignifier.turtlesize(5)
keysignifier.goto(200,0)

# Writes the words
writer = trtl.Turtle()
writer.hideturtle()
writer.penup()
writer.color('green')
writer.goto(200,-50)

# For the timer
fontsetup = ('Arial',35,'normal')

timekeeper = trtl.Turtle()
timekeeper.hideturtle()
timekeeper.penup()
timekeeper.color('red')
timekeeper.goto(0,-200)


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
    painter.goto(-110,-30)
    painter.pendown()
    painter.setheading(60)
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
    painter.goto(-180,50)
    painter.pencolor('black')
    painter.pendown()

    for i in range(5):
        painter.forward(75)
        painter.right(144)
        painter.forward(75)
        painter.left(72)

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
    painter.goto(-100,50)

    # Top half
    painter.pendown()
    painter.setheading(90)
    painter.circle(100,180)

    painter.setheading(0)
    for i in range(7):
        painter.left(45)
        painter.forward(20)
        painter.right(90)
        painter.forward(20)
        painter.setheading(0)
    painter.penup()

    # Handle
    painter.goto(-200,58)
    painter.setheading(270)
    painter.pendown()
    painter.forward(120)
    painter.circle(-20,180)



def draw_crack(life):
    if life >= 2:
        painter.goto(-200,-125)
        for i in range(5):
            painter.pendown()
            painter.setheading(45)
            painter.forward(10)
            painter.setheading(90)
            painter.forward(15)
            painter.penup()
            painterxposition = painter.xcor()
            painteryposition = painter.ycor()
    elif life < 2:
        for i in range(4):
            painter.pendown()
            painter.setheading(45)
            painter.forward(5)
            painter.setheading(90)
            painter.forward(20)
            painter.penup()
    
def draw_lose():
    painter.clear()
    painter.setheading(0)
    painter.goto(-200, -125)

    painter.pendown()
    painter.circle(150,180)

#-------FUNCTIONS-------
def select_shape(x,y): # Responsible for starting the game
    global starting
    cookieselection = rand.randint(1,4)
    starting = False
    
    return cookieselection

def draw_shape(num):
    # The number that'll set how many letters are to be pressed for each shape: removing any letters after the number
    cap = 0
    if num == 1:
        draw_triangle()
        cap = 55
    elif num == 2:
        draw_circle()
        cap = 65
    elif num == 3:
        draw_star()
        cap = 80
    elif num == 4:
        draw_umbrella()
        cap = 90 
    
    list_cap(cap)

def list_cap(caplength):
    donecap = False
    while donecap == False:
        if len(letter_list) != caplength:
            indexrand = rand.randint(0,len(letter_list)-1)
            letter_list.pop(indexrand)

        else:
            donecap = True

def check_key(key):
    # Dont need 'global currentletter' as the variable isn't being changed
    if currentletter.lower() == key:
        reset_letter()
    elif currentletter.lower() != key:
        if lives > 0:
            lives_handler()

def draw_letter(letter):
    keysignifier.showturtle()
    writer.clear()
    writer.write(letter, align='center',font=('Arial', 100, 'normal'))

def reset_letter():
    global currentletter
    index = rand.randint(0,len(letter_list)-1)

    if len(letter_list) > 1:
        currentletter = letter_list.pop(index)
        draw_letter(currentletter)
    else:
        game_end(True, False) # The letters ran out

def timer():
    global totaltime

    if gamefin == False:
        if totaltime <= 0:
            game_end(False, True) # Winning the game is false, but the time ran out initiating a game end
        else:
            timekeeper.clear()
            timekeeper.write(str(totaltime) + ' seconds left',align='center', font=fontsetup)
            totaltime -= 1
            timekeeper.getscreen().ontimer(timer, counter_interval)

def lives_handler():
    global lives

    lives -= 1
    print('lost a life: down to ', lives, ' left')
    if lives < 1:
        game_end(False, False) # Both winning the game and the timer being up is false
    else:
        draw_crack(lives)
    
def game_end(win, timerup):
    global letter_list, gamefin
    
    gamefin = True

    letter_list = list()
    writer.clear()
    keysignifier.hideturtle()

    if win == True and timerup == False: # Won the game fully
        print('winner!')
    elif win == False and timerup == True: # Ran out of time
        timekeeper.clear()
        timekeeper.write('OUT OF TIME', align='center',font=fontsetup)
        draw_lose()
        
    elif win == False and timerup == False: # Ran out of lives
        timekeeper.clear()
        draw_lose()

# TODO 9: make the lines on the cookie line up matching up with the amount of keys pressed

# TODO ???: SCORE SYSTEM CAN BE ACCULMATED BY THE AMOUNT OF KEYS PRESSED

'''
pressed right key: +10
pressed wrong key: -5
final score multiplied by amount of time left
type of cookie = a bonus multiplier
'''


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
draw_letter(currentletter)
timer()


for letter in 'qwertyuiopasdfghjklzxcvbnm':
    wn.onkeypress(lambda l=letter: check_key(l), letter)

# lambda is essentially creating a function with a singular parameter, giving it to the check_key() function



#--------SCREEN--------
# TODO 9: Win screen, showing the cookie being cracked? Displaying points and name










wn.mainloop()












# TODO OPTIONAL (10): Turtle tracing the shape of the cookie as keys are being pressed (OPTIONAL)

# TODO 11: Leaderboard (Create a txt file)
