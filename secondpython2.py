#x = input('What is your first integer? ')
#a = int(x)

#x = input("What is your second integer? ")
#b = int(x)

#print(a*b)

#import time

#input("press enter and count up to 20 seconds.")
#start = time.time()

#input("press enter again after 20 seconds.")
#end = time.time()

#et = end - start
#print("actual time span:", et, "seconds")
#print("difference:", abs(et - 20), "seconds")

x = input("12+23=")
a = int(x)

if a == 12+23:
    print('Nice!')
else:
    print('please try again')
    x = input("12+23=")
    a = int(x)
    if a == 12+23:
          print('Now you are correct!')
    else:
          print('please try again!')
