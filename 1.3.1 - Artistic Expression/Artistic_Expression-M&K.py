import turtle as trtl


#----SCREEN SETUP----
wn = trtl.Screen()



#----IMAGE SETUP-----
envelope_closed = 'closedenveloperesize.gif'
wn.addshape(envelope_closed)

envelope_opened = 'openenveloperesize.gif'
wn.addshape(envelope_opened)



#-----TURTLES-----
envelope = trtl.Turtle(shape=envelope_closed) # Envelope picture at the beginning. originally set to closed (shape=)


#-----FUNCTIONS-----
def open(x,y): # onclick gives 2 parameters but they're not necessary to use
    envelope.shape(envelope_opened)



#----EVENTS----
envelope.onclick(open)




# TODO 3: Import the puzzle pieces images, creating different turtles for each
# TODO 3.1: Store all the puzzle pieces in a list

# TODO 4: Have the puzzle pieces come out of the envelope and go to different places (function)

# TODO 5: Make each puzzle piece able to be dragged

# TODO 6: Conditional statement if the puzzle piece comes close enough to a (x,y) coordinate and disabling the drag function

# TODO 7: Option to restart the puzzle?

# TODO 8: Make everything clearly able to be read/seen by an elderly person











wn.mainloop()