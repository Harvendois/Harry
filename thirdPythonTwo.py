import random

def cointoss():

    input("toss coin(enter)")
#input 에 value가 없으면 enter 인듯


    coin = random.randrange(2)
    x = int(coin)

    if x==0:
        print('front')
                
    else:
        print('back')

    q=input("toss again?")
    if q=="y":
        cointoss()
