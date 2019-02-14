import random

def makeQuestion():
    a = random.randint(1,40)
    b = random.randint(1,20)
    op = random.randint(1,3)

    q = str(a)

    if op == 1:
        q = q + "+"
    if op == 2:
        q = q + "-"
    if op == 3:
        q = q + "*"

    q = q + str(b)

    return q



sc1 = 0
sc2 = 0

import time

input("Press enter to start the math quiz")
start = time.time()


for x in range(5):
    q = makeQuestion()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r:
        print("correct!")
        sc1 = sc1 + 1
    else:
        print("wrong!")
        sc2 = sc2 + 1

input("Press enter to end the math quiz")
end = time.time()

et = end - start

print("correct answers:", sc1, "wrong answers:", sc2, "time spent:", et)
if sc2 == 0:
    print("great job!")
