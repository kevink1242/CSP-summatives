import turtle as trtl
import random as rand

#-----SCREEN SETUP-----
wn = trtl.Screen()

wn.setup(width=750, height=600)
wn.cv._rootwindow.resizable(False, False)

#------VARIABLES-----
xcord = -265

letter_list = list('QWERTYUIOPASDFGHJKLZXCVBNMWERTYUIOPASDFGHJKLZXCVBQWERTYUIOPASDFGHJKLZXCVBNMWERTYUIOPASDFGH') # = 90 letters
currentletter = 'E'

lettercount = 0 # Handles switching sides for each shapes outline

lives = 3

# Timer
totaltime = 50
counter_interval = 1000


gamefin = False # Variable for if the game is finished
# Essentially only purpose is for the timer. Fixed the issue of the timer counting down even after finishing the game


# Win screen
maxchar = 12
username = trtl.textinput('Player name','What is your name?')
username = username[:maxchar] # Limits the amount of characters that can be used

useridentity = rand.randint(1,255)
if useridentity == 255:
    useridentity += 201 # Gives the small chance to be player 456
elif useridentity < 100:
    if useridentity < 10:
        useridentity = '00'+str(useridentity) # adds a 0 in front of the number to make the number look more accurate to squid games
    else:
        useridentity = '0'+str(useridentity) # likewise line 39

    

score = 0

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

# Specifically to draw the cracks as the user loses lives
crackpainter = trtl.Turtle()
crackpainter.penup()
crackpainter.hideturtle()
crackpainter.speed(0)
crackpainter.pensize(penS)
crackpainter.pencolor('black')

# For the actual game part of the program 
keysignifier = trtl.Turtle(shape='circle')
keysignifier.hideturtle()
keysignifier.penup()
keysignifier.color('lightgray')
keysignifier.turtlesize(5)
keysignifier.goto(200,0)

# Writes the words/letters
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

# Soley for the 'menu screen' giving instructions
instructioner = trtl.Turtle()
instructioner.penup()
instructioner.hideturtle()
instructioner.color('black')
instructioner.goto(0,150)

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
    painter.goto(-200,-85)

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
    painter.goto(-110,-30)
    painter.setheading(180)

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
    painter.penup()
    painter.setheading(0)
    painter.goto(-180,50)

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
    painter.penup()

def draw_crack(life):
    if life >= 2:
        crackpainter.goto(-200,-125)
        for i in range(5):
            crackpainter.pendown()
            crackpainter.setheading(45)
            crackpainter.forward(10)
            crackpainter.setheading(90)
            crackpainter.forward(15)
            crackpainter.penup()
    elif life < 2:
        for i in range(4):
            crackpainter.pendown()
            crackpainter.setheading(45)
            crackpainter.forward(5)
            crackpainter.setheading(90)
            crackpainter.forward(20)
            crackpainter.penup()
    
def draw_lose():
    painter.clear()
    crackpainter.clear()

    crackpainter.setheading(0)
    crackpainter.goto(-200, -125)
    crackpainter.pendown()
    crackpainter.circle(150,147)
    crackpainter.penup()
    crackpainter.setheading(180)
    crackpainter.goto(-220,-125)
    crackpainter.pendown()
    crackpainter.circle(-150,210)

#----------OUTLINING----------
def outline_circle():
   painter.pencolor('chartreuse')
   painter.pendown()
   painter.circle(100,6)

def outline_triangle(side):
    if side == 1:
        painter.pencolor('chartreuse')
        painter.pendown()
        painter.forward(9.5)
    if side == 2:
        painter.setheading(60)
        painter.forward(9.5)
    if side == 3:
        painter.setheading(300)
        painter.forward(3.5)

def outline_star(side):
    painter.pencolor('chartreuse')
    painter.pendown()
    if side == 1:
        painter.forward(9)
    elif side == 2:
        painter.setheading(213)
        painter.forward(9)
    elif side == 3:
        painter.setheading(287)
        painter.forward(11)
    elif side == 4:
        painter.setheading(149)
        painter.forward(9)
    elif side == 5:
        painter.setheading(220)
        painter.forward(9)
    elif side == 6:
        painter.setheading(70)
        painter.forward(9)
    elif side == 7:
        painter.setheading(144)
        painter.forward(15)
    elif side == 8:
        painter.setheading(0)
        painter.forward(9)
    elif side == 9:
        painter.setheading(74)
        painter.forward(9)
    elif side == 10:
        painter.setheading(293)
        painter.forward(9)



#-------FUNCTIONS-------
def select_shape(x,y): # Responsible for starting the game
    global starting
    cookieselection = rand.randint(1,4)
    starting = False
    
    return cookieselection

def draw_shape(num):
    instructioner.clear()

    cap = 0 # The number that'll set how many letters are to be pressed for each shape: removing any letters after the number
    if num == 1:
        draw_triangle()
        cap = 55
    elif num == 2:
        draw_circle()
        cap = 60
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
    global lettercount, score
    # Dont need 'global currentletter' as the variable isn't being changed
    if currentletter.lower() == key:
        outline_handler(userselection)
        lettercount += 1

        reset_letter()
        score += 10
    elif currentletter.lower() != key:
        if lives > 0:
            lives_handler()
        score -= 5

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

def outline_handler(cookie):
    if cookie == 1: # Triangle cookie
        triangleside = 1
        if lettercount == 18:
            triangleside = 2
            outline_triangle(triangleside)
        elif lettercount == 36:
            triangleside = 3
            outline_triangle(triangleside)
        else:
            outline_triangle(triangleside)

    elif cookie == 2: # Circle cookie
        outline_circle()

    elif cookie == 3: # Star cookie
        starside = 1
        if lettercount == 8:
            starside = 2
            outline_star(starside)
        elif lettercount == 16:
            starside = 3
            outline_star(starside)
        elif lettercount == 24:
            starside = 4
            outline_star(starside)
        elif lettercount == 32:
            starside = 5
            outline_star(starside)
        elif lettercount == 40:
            starside = 6
            outline_star(starside)
        elif lettercount == 48:
            starside = 7
            outline_star(starside)
        elif lettercount == 56:
            starside = 8
            outline_star(starside) 
        elif lettercount == 64:
            starside = 9
            outline_star(starside)
        elif lettercount > 71:
            starside = 10
            outline_star(starside)
        else:
            outline_star(starside)
    elif cookie == 4:
        print('umbrella outline')

def game_end(win, timerup):
    global letter_list, gamefin
    
    gamefin = True

    letter_list = list()
    writer.clear()
    keysignifier.hideturtle()
    timekeeper.clear()

    if win == True and timerup == False: # Won the game fully
        win_screen()
    elif win == False and timerup == True: # Ran out of time
        writer.pencolor('red')
        writer.goto(160,0)
        writer.write('PLAYER '+str(useridentity)+' HAS LOST',align='center',font=fontsetup)
        timekeeper.write('OUT OF TIME', align='center',font=fontsetup)
        draw_lose()
    elif win == False and timerup == False: # Ran out of lives
        writer.pencolor('red')
        writer.goto(160,0)
        writer.write('PLAYER '+str(useridentity)+' HAS LOST',align='center',font=fontsetup)
        draw_lose()

def win_screen():                                                       
    writer.pencolor('black')
    # Address the user
    writer.goto(150,120)
    writer.write('Congrats '+username+', Player '+str(useridentity), align='center',font=('Arial',25,'normal'))
    #-------------------------- Setting final score
    shapemultiplier = userselection*1000
    timemultiplier = totaltime*10
    lifemultiplier = lives*5

    finalscore = score+shapemultiplier+timemultiplier+lifemultiplier
    #-------------------------
    writer.goto(150,90)
    writer.write('Your score was: '+str(finalscore)+'!',align='center',font=('Arial',23,'normal'))

    # Address the different multipliers to the user
    writer.pencolor('firebrick4')
    writer.goto(150,30)
    writer.write('Initial score: '+str(score), align='center',font=('Arial',22,'normal'))

    writer.goto(150,0)
    if userselection == 1:
        writer.write('Triangle shape +1000', align='center',font=('Arial',22,'normal'))
    elif userselection == 2:
        writer.write('Circle shape +2000', align='center',font=('Arial',22,'normal'))
    elif userselection == 3:
        writer.write('Star shape +3000', align='center',font=('Arial',22,'normal'))
    elif userselection == 4:
        writer.write('Umbrella shape +4000', align='center',font=('Arial',22,'normal'))
    
    writer.goto(150,-30)
    writer.write('+'+str(totaltime)+' seconds left x10',align='center',font=('Arial',22,'normal'))

    writer.goto(150,-60)
    writer.write('+'+str(lives)+' lives left x5',align='center',font=('Arial',22,'normal'))
    

# TODO 9: make the lines on the cookie line up matching up with the amount of keys pressed

#----------GAME-----------

# Pauses the program from continuing and assigning a value to 'userselection'
starting = True # Variable is set to false in the select_shape function

# Writing 'instructions' on the screen for clarity
instructioner.write('Welcome Player '+str(useridentity)+', please select a cookie',align='center',font=fontsetup)
instructioner.goto(0,-150)
instructioner.write('Each cookie will have a different shape,', align='center',font=('Arial',20,'normal'))
instructioner.goto(0,-170)
instructioner.write('requiring you to click an amount of keys ranging in difficulty',align='center',font=('Arial',20,'normal'))

while starting:
    placeholder_list[0].onclick(select_shape)
    placeholder_list[1].onclick(select_shape)
    placeholder_list[2].onclick(select_shape)
    placeholder_list[3].onclick(select_shape)

# After exiting the while loop, the userselection variable is assigned a variable based on the return from the function
userselection = select_shape(0,0)

for d in placeholder_list:
    d.hideturtle()
    

# Activating functions
draw_shape(userselection)
draw_letter(currentletter)
timer()

wn.listen() # Had to be moved down here because trtl.textinput was messing with the onkeypress

for letter in 'qwertyuiopasdfghjklzxcvbnm':
    wn.onkeypress(lambda l=letter: check_key(l), letter)

# lambda is essentially creating a function with a singular parameter, giving it to the check_key() function













wn.mainloop()