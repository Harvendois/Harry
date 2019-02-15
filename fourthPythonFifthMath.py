import math

d = [1,2,3,4,5]
print(d)

#sum
mean = sum(d) / len(d)
print(mean)

#mean v=variation
vsum = 0
for x in d:
    vsum = vsum + (x - mean)**2
var = vsum / len(d)
print(var)

#std
std = math.sqrt(var)
print(std)

#import math
def quadraticCalc():
    import sys

    print("ax2 + bx + c = 0")
    a = float(input("a? "))
    b = float(input("b? "))
    c = float(input("c? "))

    if a == 0:
        print("a=0: not a quadratic equation.")
        sys.exit()

    D = b*b - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print("2 solutions:", x1, x2)
    if D == 0:
        x = -b/(2*a)
        print("1 solution:", x)
    if D < 0:
        print("no solution.")

#drawing graph program
import turtle as t

#range of x for graph
xMin=-5
xMax=5

#range of y for graph
yMin=-5
yMax=5

#space between graph
space = 0.01

#list of function to draw
funcList = ["y=x*x", "y=abs(x)", "y=0.5*x + 1"]

#coordination setting, turtle speed, line width
t.setworldcoordinates(xMin, yMin, xMax, yMax)
t.speed(0)
t.pensize(2)

#drawing x axis
t.up()
t.goto(xMin,0)
t.down()
t.goto(xMax,0)

#drawing y axis
t.up()
t.goto(0, yMin)
t.down()
t.goto(0, yMax)

#drawing graph
t.color("green")
for func in funcList:
    x = xMin
    exec(func)
    t.up()
    t.goto(x,y)
    t.down()
    while x <= xMax:
        x = x + space
        exec(func)
        t.goto(x,y)

#to find out the x intercept of y or other lines, i think we will use if..t.write()
        # we should also let it keep going with 'while' just like the turtle game
