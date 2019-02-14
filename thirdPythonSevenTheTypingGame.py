import random
import time

animals = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n = 1
print("press enter to start the typing game")
input()
start = time.time()



q = random.choice(animals)
while n<= 5:
    print("number", n)
    print(q)
    x = input()
    if q == x:
        print('great!')
        n = n+1
        q = random.choice(animals)
    else:
        print("wrong! type again!")

end = time.time()
et = end - start
et = format(et, ".2f")
print("your time spent:", et, "seconds")
    
