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

puzzlepiece_list = [puzzlepiece1,puzzlepiece2,puzzlepiece3,puzzlepiece4,puzzlepiece5,puzzlepiece6]



#-----FUNCTIONS-----
def open(x,y): # onclick gives 2 parameters but they're not necessary to use
    envelope.shape(envelope_opened)

    index = 0
    for i in puzzlepiece_list:
        randx = rand.randint(-400,400)
        randy = rand.randint(-400,400)

        puzzlepiece_list[index].showturtle()
        puzzlepiece_list[index].goto(randx,randy)
        puzzlepiece_list[index].speed(0)

        index += 1
    envelope.goto(0,800)

def objectdrag(x,y, piece):
    piece.goto(x,y)

#----EVENTS----
envelope.onclick(open)

puzzlepiece1.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece1))
puzzlepiece2.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece2))
puzzlepiece3.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece3))
puzzlepiece4.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece4))
puzzlepiece5.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece5))
puzzlepiece6.ondrag(lambda x,y: objectdrag(x,y,puzzlepiece6))




# TODO 3: Import the puzzle pieces images, creating different turtles for each
# TODO 3.1: Store all the puzzle pieces in a list

# TODO 4: Have the puzzle pieces come out of the envelope and go to different places (function)

# TODO 5: Make each puzzle piece able to be dragged

# TODO 6: Conditional statement if the puzzle piece comes close enough to a (x,y) coordinate and disabling the drag function

# TODO 7: Option to restart the puzzle?

# TODO 8: Make everything clearly able to be read/seen by an elderly person











wn.mainloop()