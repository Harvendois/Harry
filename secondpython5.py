import random

a = random.randint(1,99)
b = random.randint(1,99)

print("What is the sum of", a, "+", b, "?")
x = input()
c = int(x)

#input expected at most 1 arguments, got 5

if a+b == c:
    print('great job!')
else:
    print('please run this again')
