import turtle as t
import random

score = 0
playing = False

tn = t.Turtle()
tn.shape("turtle")
tn.color("red")
tn.speed(0)
tn.up()
tn.goto(0,200)

tn2 = t.Turtle()
tn2.shape("turtle")
tn2.color("blue")
tn2.speed(0)
tn2.up()
tn2.goto(0,200)


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

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def play():
    global score
    global playing
    t.fd(15)
    if random.randint(1, 5) == 3:
        ang = tn.towards(t.pos())
        ang = tn2.towards(t.pos())
        tn.setheading(ang)
        tn2.setheading(ang)
    speed = score + 5
    if speed > 15:
        speed = 15
    tn.forward(speed)
    tn2.forward(speed)
    if t.distance(tn) < 12:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0
    if t.distance(tn2) < 12:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0
    if t.distance(tp) < 12:
        score = score + 1
        t.write(score, "top")
        starX = random.randint(-230,230)
        starY = random.randint(-230,230)
        tp.goto(starX, starY)
    if playing:
        t.ontimer(play,100)

def message(m1, m2):
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run")
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
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")

