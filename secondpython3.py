import turtle as t
import random

t.shape('turtle')
t.speed(0)

#t.setheading(a) a 각도로 방향을 돌림

for x in range(500):
    a = random.randint(1, 360)
    t.setheading(a)
    t.forward(10)

    
