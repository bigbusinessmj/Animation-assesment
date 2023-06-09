#first change after syncing to local mac repo and commiting within visual code studio - just this comment
#second change made after loading into V
#import needed libraries   
import turtle
from turtle import *
import random
#added code to change ball to random color each time it hits a wall
#added code to change border size when user presses spacebar
#Define constants
RIGHT_EDGE= 400
LEFT_EDGE = -400
BOTTOM_EDGE = -400
TOP_EDGE = 400

GRAVITY = -.1 #made gravity negative to reverse the y direction effect the gravity has
DAMPING = .8
FRICTION = .02

#This function will update the location of the ball
def moveBall():
    global xVel, yVel

    #update the postiion of the ball
    x = ball.xcor()
    if xVel != 0: # we have not stopped rolling due to friction
        ball.setx(x + xVel)
        
    y = ball.ycor()
    if yVel!=0: #if it's 0 we are not bouncing, we are rolling
        yVel = yVel - GRAVITY   #only y is impacted by gravity
        ball.sety(y + yVel)
    else:   # friction comes into play while rolling which impacts xVel
        if (xVel>0):  xVel = xVel-FRICTION
        if (xVel<0):  xVel = xVel+FRICTION
        if abs(xVel)>.005:  #we are still rolling
            # print(xVel) - debug
            pass
        else:  # we are done - ball stopped bouncing and then stopped rolling
            exit()

    #Check for collisons and reverse the direction if so
    if (x >= RIGHT_EDGE):
        xVel *= -1
        RLcolors = ["blue", "red", "yellow", "brown"]
        ball.color(random.choice(RLcolors))
        if xVel!=0:
            ball.setx(x + xVel-5)

    if (x <= LEFT_EDGE):
        xVel *= -1
        RLcolors = ["blue", "red", "yellow", "brown"]
        ball.color(random.choice(RLcolors))
        if xVel!=0:
            ball.setx(x + xVel+5)
   
    if (y <= BOTTOM_EDGE):
        yVel *= -1
        TBcolors = ["chocolate", "skyblue", "yellow"]
        ball.color(random.choice(TBcolors))
        ball.sety(y + yVel-5)

    if (y >= TOP_EDGE + 5):
        yVel *= -1
        TBcolors = ["chocolate", "skyblue", "yellow"]
        ball.color(random.choice(TBcolors))
        #switched damping effect from the bottom edge to the top edge
        yVel = yVel * DAMPING #damping effect
        if yVel>2:
            ball.sety(y + yVel+5)
        else:
            yVel=0

def spacebarpress():  #created a function to call from the main program and to use in the onkey command to make things easier
    global RIGHT_EDGE, LEFT_EDGE, TOP_EDGE, BOTTOM_EDGE #needed global variables to bring the border values inside the function
    
    #all the code in this function does is check whether the borders are normal or smaller and if the user presses spacebar it switches to the other size
    if RIGHT_EDGE == 400:
        RIGHT_EDGE = 175
    else:
        RIGHT_EDGE = 400
    if LEFT_EDGE == -400:
        LEFT_EDGE = -175
    else:
        LEFT_EDGE = 400
    if TOP_EDGE == 400:
        TOP_EDGE = 175
    else:
        TOP_EDGE = 400
    if BOTTOM_EDGE == -400:
        BOTTOM_EDGE = -175
    else:
        BOTTOM_EDGE == -400

    

#Global variables
screen = Screen()
screen.title("My window")
screen.bgcolor("green")

ball = Turtle()
ball.clear()
ball.penup()

ball.shape("circle")
ball.color("blue")
ball.position()
ball.speed(0)
ball.setheading(40)

#Define initial position and speed of the ball
ball.setx(100)
ball.sety(200)
xVel = 5
yVel = 3

screen.tracer(0) #turn off auto screen updates to make it faster

turtle.onkey(spacebarpress,"space") #linking the spacebar function to the spacebar key so that when the user presses space the function comes into effect

while True:
    moveBall()
    screen.update()
    spacebarpress() #calling the spacebar function
   
