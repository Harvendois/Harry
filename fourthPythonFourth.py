A = {1,2,3,4}
B = {3,4,5,6}

print(A)
print(B)
print(len(A))

print(A | B)
print(A & B)
print (A - B)

C = {x for x in range(1,11)}
D = {x for x in range(1,11) if x % 3 == 0}

print(C)
print(D)

print(C<D)
print(C>D)

#소인수분해 프로그램

def fractionalDecomp():
    x = int(input("? "))
    d = 2

    while d <= x:
        if x % d == 0:
            print(d)
            x = x/d
        else:
            d = d + 1



