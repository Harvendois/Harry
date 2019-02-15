import turtle as t
import random

#characters

tn = t.Turtle()
tn.shape("turtle")
tn.color("red")
tn.speed(0)
tn.up()
tn.goto(0,200)


tp = t.Turtle()
tp.shape("circle")
tp.color("green")
tp.speed(0)
tp.up()
tp.goto(0,-200)


def turnRight():
    t.setheading(0)

def turnUp():
    t.setheading(90)

def turnLeft():
    t.setheading(180)

def turnDown():
    t.setheading(270)

def play():
    t.fd(10)
    ang = tn.towards(t.pos())
    tn.setheading(ang)
    tn.fd(9)
    if t.distance(tp) < 12:
        starX = random.randint(-230, 230)
        starY = random.randint(-230, 230)
        tp.goto(starX, starY)
        n = 0
        n = n+1
        t.write(n, False, "center", ("", 15))
    if t.distance(tn) >= 12:
        t.ontimer(play, 100)

t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turnRight, "Right")
t.onkeypress(turnUp, "Up")
t.onkeypress(turnLeft, "Left")
t.onkeypress(turnDown, "Down")
t.listen()
play()
