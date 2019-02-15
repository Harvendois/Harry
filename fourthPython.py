import turtle as t
#t.up()
#t.goto(100,50)
#t.pos()

#t.write("my oh my", False, "center", ("", 15))

import random

def turnUp():
    t.left(2)

def turnDown():
    t.right(2)

def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(20)
        t.right(5)

    d = t.distance(target, 0)
    t.sety(random.randint(10,100))
    while d < 25:
        t.color("blue")
        t.write("Good!", False, "center", ("",15))
    else:
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
    t.color("black")
    t.goto(-200, 10)
    t.setheading(ang)


#ground
t.goto(-300,0)
t.down()
t.goto(300,0)

#drawing target
target = random.randint(50,250)
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

#turtle in the beginning of the game
t.color("black")
t.up()
t.goto(-200,10)
t.setheading(20)

#movement settings - keyboard
t.onkeypress(turnUp, "Up")
t.onkeypress(turnDown, "Down")
t.onkeypress(fire, "space")
t.listen()

#space has to be "space" not "Space"
