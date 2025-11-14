import turtle as trtl
import random as rand


#----SCREEN SETUP----
wn = trtl.Screen()

wn.setup(width=900, height=800)
wn.cv._rootwindow.resizable(False, False)



#----IMAGE SETUP-----
envelope_closed = 'closedenveloperesize.gif'
wn.addshape(envelope_closed)

envelope_opened = 'openenveloperesize.gif'
wn.addshape(envelope_opened)

piece1 = '1.gif'
wn.addshape(piece1)

piece2 = '2.gif'
wn.addshape(piece2)

piece3 = '3.gif'
wn.addshape(piece3)

piece4 = '4.gif'
wn.addshape(piece4)

piece5 = '5.gif'
wn.addshape(piece5)

piece6 = '6.gif'
wn.addshape(piece6)


#-----TURTLES-----
drawer = trtl.Turtle()
drawer.pensize(10)
drawer.pencolor('lightsalmon4')
drawer.speed(0)
drawer.penup()
drawer.hideturtle()

envelope = trtl.Turtle(shape=envelope_closed) # Envelope picture at the beginning. originally set to closed (shape=)
envelope.penup()

puzzlepiece1 = trtl.Turtle(shape=piece1)
puzzlepiece1.penup()
puzzlepiece1.hideturtle()

puzzlepiece2 = trtl.Turtle(shape=piece2)
puzzlepiece2.penup()
puzzlepiece2.hideturtle()

puzzlepiece3 = trtl.Turtle(shape=piece3)
puzzlepiece3.penup()
puzzlepiece3.hideturtle()

puzzlepiece4 = trtl.Turtle(shape=piece4)
puzzlepiece4.penup()
puzzlepiece4.hideturtle()

puzzlepiece5 = trtl.Turtle(shape=piece5)
puzzlepiece5.penup()
puzzlepiece5.hideturtle()

puzzlepiece6 = trtl.Turtle(shape=piece6)
puzzlepiece6.penup()
puzzlepiece6.hideturtle()


#---LISTS---
puzzlepiece_list = [puzzlepiece1,puzzlepiece2,puzzlepiece3,puzzlepiece4,puzzlepiece5,puzzlepiece6]

cords_list = [(-150,69),(-2,53),(142,52),(-150,-56),(1,-78),(140,-75)]

# coordinates match the puzzle piece in the same index
# Each set of coordinates is a "tuple"


#-----FUNCTIONS-----
def open(x,y): # onclick gives 2 parameters but they're not necessary to use
    envelope.shape(envelope_opened)

    index = 0
    for i in puzzlepiece_list:

        randx = rand.randint(-400,400)
        randy = rand.randint(-400,400)

        puzzlepiece_list[index].showturtle()
        puzzlepiece_list[index].speed(7)
        puzzlepiece_list[index].goto(randx,randy)
        puzzlepiece_list[index].speed(0)

        index += 1
    envelope.hideturtle()
    framedrawing()

def framedrawing():
    drawer.goto(-230,150)
    drawer.pendown()
    drawer.forward(440)
    drawer.setheading(270)
    drawer.forward(295)
    drawer.setheading(180)
    drawer.forward(440)
    drawer.setheading(90)
    drawer.forward(295)

def objectdrag(x,y, piece):
    selectedpiece = puzzlepiece_list.index(piece) # Acts as the index for the different tuples themselves inside of cords_list
    piece.goto(x,y)
    

    print('is at',x,',',y)

    # the number inside of the second bracket is the index for the inside of the tuple
    if ((piece.xcor()-25) < cords_list[selectedpiece][0]) and ((piece.xcor()+25) > cords_list[selectedpiece][0]):
        if ((piece.ycor()-25) < cords_list[selectedpiece][1]) and ((piece.ycor()+25) > cords_list[selectedpiece][1]):
            print('done')
            if selectedpiece == 0:
                puzzlepiece1.goto(cords_list[0])
                puzzlepiece1.ondrag(None)
            elif selectedpiece == 1:
                puzzlepiece2.goto(cords_list[1])
                puzzlepiece2.ondrag(None)
            elif selectedpiece == 2:
                puzzlepiece3.goto(cords_list[2])
                puzzlepiece3.ondrag(None)
            elif selectedpiece == 3:
                puzzlepiece4.goto(cords_list[3])
                puzzlepiece4.ondrag(None)
            elif selectedpiece == 4:
                puzzlepiece5.goto(cords_list[4])
                puzzlepiece5.ondrag(None)
            elif selectedpiece == 5:
                puzzlepiece6.goto(cords_list[5])
                puzzlepiece6.ondrag(None)
    else:
        print('not')

#----PROGRAM----
envelope.onclick(open)


# lambda creates a third 'anonymous' variable that allows for the ondrag() function to give 3 parameters instead of 2
puzzlepiece1.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece1))
puzzlepiece2.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece2))
puzzlepiece3.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece3))
puzzlepiece4.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece4))
puzzlepiece5.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece5))
puzzlepiece6.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece6))





# TODO 7: Option to restart the puzzle?

# TODO 8: Make everything clearly able to be read/seen by an elderly person











wn.mainloop()