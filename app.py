import turtle

wind=turtle.Screen()
wind.title("Ping Pong by MS")
wind.bgcolor("black")  #background color
wind.setup(width=800,height=600)
wind.tracer(0)   #stops the window from updating automatically

#madrab1
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5,stretch_len=1) #stretch by factor (the initial size is 20 x 20 pixels/)
madrab1.penup()
madrab1.goto(-380,0)

#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1) #stretch by factor (the initial size is 20 x 20 pixels/)
madrab2.penup()  #stops the obj from drawing lines
madrab2.goto(370,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .2
ball.dy = .2

#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0  Player 2:0",align="center",font=("courier",24,"normal"))

#functions
def madrab1_up():
    y=madrab1.ycor()
    y+=20
    madrab1.sety(y)

def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)

def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)

def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)

#keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")


#main game loop
while True:
    wind.update()


    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check  
    if (ball.ycor()>290):#the ball radius is 10 pexels
        ball.sety(290)
        ball.dy *= -1

    if (ball.ycor()<-290):#the ball radius is 10 pexels
        ball.sety(-290)
        ball.dy *= -1

    if(ball.xcor()>390):
        ball.goto(0,0)
        ball.dx *=-1
        score1+=1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))

    if(ball.xcor()<-390):
        ball.goto(0,0)
        ball.dx *=-1
        score2+=1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))


    if(ball.xcor()>-380 and ball.xcor()<-370 and ball.ycor()>madrab1.ycor()-40 and ball.ycor()<madrab1.ycor()+40):
        ball.setx(-370)
        ball.dx *=-1

    if(ball.xcor()>360 and ball.xcor()<370 and ball.ycor()>madrab2.ycor()-40 and ball.ycor()<madrab2.ycor()+40):
        ball.setx(360)
        ball.dx *=-1
