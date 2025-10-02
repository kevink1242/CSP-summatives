import turtle as trtl
painter = trtl.Turtle()
painter.speed(0.3)
painter.shapesize(6)


#-------------------------- Eye definitions
def eyes_regular():
    painter.pencolor('white')
    painter.fillcolor('white')

    painter.goto(-20,80)
    painter.pendown()
    painter.begin_fill()
    painter.circle(19)
    painter.end_fill()
    painter.penup()

    painter.goto(15,80)
    painter.pendown()
    painter.begin_fill()
    painter.circle(19)
    painter.end_fill()
    painter.penup()

    painter.fillcolor('black')

    painter.goto(-20,85)
    painter.pendown()
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()
    painter.penup()

    painter.goto(15,85)
    painter.pendown()
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()
    painter.penup()

def eyes_glasses():
    painter.pencolor('white')
    painter.fillcolor('white')

    painter.goto(-20,80)
    painter.pendown()
    painter.begin_fill()
    painter.circle(19)
    painter.end_fill()
    painter.penup()

    painter.goto(15,80)
    painter.pendown()
    painter.begin_fill()
    painter.circle(19)
    painter.end_fill()
    painter.penup()

    painter.pencolor('black')
    painter.fillcolor('black')

    painter.goto(-20,85)
    painter.pendown()
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()
    painter.penup()

    painter.goto(15,85)
    painter.pendown()
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()
    painter.penup()

    # Glasses
    painter.pensize(5)
    painter.goto(-25, 75)
    painter.pendown()
    painter.circle(25)
    painter.penup()

    painter.goto(20, 75)
    painter.pendown()
    painter.circle(25)
    painter.penup()

    painter.setheading(30)
    painter.goto(45,100)
    painter.pendown()
    painter.forward(30)
    painter.penup()

    painter.setheading(150)
    painter.goto(-45,100)
    painter.pendown()
    painter.forward(30)
    painter.penup()

    painter.pensize(2)
    painter.setheading(0)
#-------------------------- Mouth definitions
def mouth_regular():
    painter.pencolor('black')
    painter.fillcolor('red')
    
    painter.goto(0,50)
    painter.pendown()
    painter.begin_fill()
    painter.pendown()
    painter.circle(20)
    painter.end_fill()
    painter.penup()

    painter.fillcolor('white')

    painter.goto(-35,45)
    painter.setheading(270)
    painter.pendown()
    painter.begin_fill()
    painter.circle(35,180)
    painter.left(90)
    painter.forward(70)
    painter.end_fill()
    painter.penup()

def mouth_mustache():
    painter.pencolor('black')
    painter.fillcolor('red')
    
    painter.goto(0,50)
    painter.pendown()
    painter.begin_fill()
    painter.pendown()
    painter.circle(20)
    painter.end_fill()
    painter.penup()

    painter.fillcolor('white')

    painter.goto(-35,40)
    painter.setheading(270)
    painter.pendown()
    painter.begin_fill()
    painter.circle(35,180)
    painter.left(90)
    painter.forward(70)
    painter.end_fill()
    painter.penup()

    painter.fillcolor('black')

    painter.goto(0,50)
    painter.pendown()
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()

    painter.goto(10,54)
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()

    painter.goto(20,50)
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()

    painter.goto(-10,54)
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()

    painter.goto(-20,50)
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()
    painter.penup()
#-------------------------- Hat definitions
def hat_first():
    painter.pensize(5)
    painter.pencolor('black')
    painter.fillcolor('black')

    painter.goto(47,150)
    painter.setheading(90)
    painter.pendown()
    painter.begin_fill()
    painter.circle(50,180,4)
    painter.end_fill()
    painter.setheading(180)
    painter.forward(10)
    painter.right(180)
    painter.forward(120)

def hat_second():
    painter.pensize(15)
    painter.pencolor('blue')
    painter.fillcolor('blue')

    painter.goto(47,150)
    painter.setheading(90)
    painter.pendown()
    painter.begin_fill()
    painter.circle(50,180)
    painter.end_fill()
    painter.setheading(180)
    painter.forward(40)
    painter.right(180)
    painter.forward(135)

    painter.pensize(5)
    painter.pencolor('darkblue')
    painter.fillcolor('darkblue')

    painter.setheading(45)
    painter.begin_fill()
    painter.circle(15,360,4)
    painter.end_fill()
    painter.penup()


def arm():
    painter.pensize(30)
    painter.pencolor('lightgrey')
    painter.fillcolor('lightgrey')

    painter.pendown()
    painter.circle(-50,70)
    painter.penup()




potatohead_list = []



active = 'y'
while active == 'y':
    # Reset turtle
    painter.showturtle()
    painter.shapesize(6)
    painter.goto(0,0)
    painter.setheading(0)

     # Draw potato body
    painter.pensize(2)
    painter.pencolor('black')
    painter.fillcolor('tan')

    painter.begin_fill()
    painter.circle(80)
    painter.end_fill()
    painter.penup()

    # Draw potato arms
    painter.goto(90,80)
    arm()
    painter.setheading(135)
    painter.goto(-90,80)
    arm()

    # Draw potato feet
    painter.pensize(10)
    painter.fillcolor('blue')
    painter.pencolor('blue')
    
    painter.goto(-5,-30)
    painter.pendown()
    painter.begin_fill()
    painter.circle(25)
    painter.end_fill()
    painter.penup()
    painter.goto(50,-30)
    painter.pendown()
    painter.begin_fill()
    painter.circle(25)
    painter.end_fill()
    painter.penup()




    painter.setheading(0)
    painter.pensize(2)
#------------------------------------ User inputs
    eyes = trtl.textinput('Create Mr. Potato Head', 'y/n for glasses')
    if eyes == 'y':
        potatohead_list.append(eyes_glasses)
    elif eyes == 'n':
        potatohead_list.append(eyes_regular)
    elif eyes != 'y' or 'n':
        exit()
    
    mouth = trtl.textinput('Create Mr. Potato Head', 'y/n for a mustache')
    if mouth == 'y':
        potatohead_list.append(mouth_mustache)
    elif mouth == 'n':
        potatohead_list.append(mouth_regular)
    elif mouth != 'y' or 'n':
        exit()
    
    hat = int(trtl.textinput('Create Mr. Potato Head', 'type an odd or even number for a hat'))
    if hat % 2 == 0:
        potatohead_list.append(hat_first)
    elif hat % 2 > 0:
        potatohead_list.append(hat_second)
    elif hat != int:
        exit()
    
# Drawing the features    
    for i in potatohead_list:
        i()
    painter.hideturtle()

    active = trtl.textinput('Repeat', 'y/n to restart?')
    if active == 'y':
        trtl.clearscreen()
        potatohead_list = []
    else:
        print('stopped')
#----------------------------------------


















wn = trtl.Screen()
wn.mainloop()