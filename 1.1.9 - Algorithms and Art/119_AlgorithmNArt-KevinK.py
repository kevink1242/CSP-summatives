import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)



#-------------------------- Eye definitions
def eyes_regular():
    painter.pencolor('black')
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
#-------------------------- Hat definitions
def hat_first():
    painter.circle(50,360,4)
    print('first hat drawn')

def hat_second():
    painter.circle(20,180)
    print('second hat drawn')

potatohead_list = []

 # Draw potato body
painter.pensize(2)
painter.pencolor('black')
painter.fillcolor('tan')

painter.begin_fill()
painter.circle(80)
painter.end_fill()
painter.penup()

active = 'y'
while active == 'y':
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
    
    hat = int(trtl.textinput('Create Mr. Potato Head', 'type a number 1-3 for a hat'))
    if hat % 3 == 0:
        active = 'n'
        potatohead_list.append(hat_first)
    elif hat % 3 == 1:
        active = 'n'
        potatohead_list.append(hat_second)
    elif hat != int:
        exit()
        
# Drawing the features        
    for i in potatohead_list:
        i()
        potatohead_list.pop()


print(potatohead_list)



















wn = trtl.Screen()
wn.mainloop()