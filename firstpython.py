print('hello')
print('hello')
print('bello')

import turtle as t
t.shape('turtle')

#삼각형 그리기

t.color('red')
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

#사각형 그리기
t.color('black')
for t in range(3):
    t.forward(100)
    t.right(90)
    

#문 만들기
t.right(90)
t.fd(100)
t.left(90)
t.fd(30)
t.left(90)
t.pensize(7)
t.fd(50)
t.right(90)
t.fd(40)
t.right(90)
t.fd(50)

print(1, '\', 4)

t=
for i in range(8):
      x = i + 2
      t = t + 1
      for j in range(t):
          y=j+1
          print(x, "*", y, "=", (i+2)*(j+1), \t ,  end= )
      print("")


from math import *

x=1
for i in range(20):
      x = x*(20-i)

print('x! = ', x)

print(factorial(1000))
      
