# def = 함수 정의하는 파이썬 언어

def hello(): 
    print("Hello Python!")


def hello2(name):
    print('Hello', name)
          
# the name as a variable better be a string

def squareRoot(a):
    c = a**0.5
    print('The square root of', a, ' is', c)

#if c = a**1/2 will eventually produce c=a*1/2 - no idea why

import math

def areaCircle(a):
    c = math.pi * a**2
    print('The area of the circle with a radius', a, ' is', c)

def areaTriangle(b,h):
    c = 0.5*h*b
    print('The area of the triangle with the base of', b,' and the height of',
          h,' is', c)
def fahrenheitCelcius(f):
    c = (f-32)*5/9
    print('The temperature in celcius degrees which is equivalent to', f, 'fahrenheit degrees is ',
          c)

    
def bmi():
    x = input('What is your height in meter?')
    h = float(x)
    y = input('What is your weight in kilogram?')
    w = int(y)
    b=w/h
    print(b)
    
#변수가 두가지 이상일데 그 함수를 설명하는 doc 나 아니면 프린트나 input 으로
#가이드를 해줘야겠다
    

import turtle as t
t.shape('turtle')

t.up()
t.goto(100,100)
t.write("this is a positive number")

t.goto(100,0)
t.write("this is zero")

t.goto(100,-100)
t.write("this is a negative number")

t.goto(0,0)
t.down()
s = t.textinput("", "input number: ")
n = float(s)

if(n > 0):
    t.goto(100,100)

if(n == 0):
    t.goto(100,0)

if(n < 0):
    t.goto(100,-100)
