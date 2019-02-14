def sum_func(n):
    s=0
    for x in range(1, n+1):
        s = s+x
    return s

import turtle as t

def polygon(n):
    if n > 2:
        for x in range(n):
            t.forward(50)
            t.left(360/n)

    else:
        print('wrong input')

def polygon2(n,a):
    for x in range(n):
        t.fd(a)
        t.left(360/n)

t.bgcolor("black")
t.speed(0)

for x in range(200):
    if x % 3 == 0:
        t.color("red")
    if x % 3 == 1:
        t.color("yellow")
    if x % 3 == 2:
        t.color("blue")
    t.fd(x * 2)
    t.left(119)
