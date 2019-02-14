import turtle as t

def turnRight():
    t.setheading(0)
    t.fd(10)
def turnUp():
    t.setheading(90)
    t.fd(10)
def turnLeft():
    t.setheading(180)
    t.fd(10)
def turnDown():
    t.setheading(270)
    t.fd(10)
def blank():
    t.clear()

t.shape("turtle")
t.color("blue")
t.speed(0)
t.onkeypress(turnRight, "Right")
t.onkeypress(turnUp, "Up")
t.onkeypress(turnLeft, "Left")
t.onkeypress(turnDown, "Down")
t.onkeypress(blank, "Escape")
t.listen()
