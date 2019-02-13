import random

n=random.randint(1,30)

while True:
    x=input("take a guess!")
    y=int(x)
    if y==n:
        print('awesome!')
        break
    if y>n:
        print('the conjectured integer is too big!')
    if y<n:
        print('the conjectured integer is too small!')
