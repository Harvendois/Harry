def bmi():
    x = input('What is your height in meter?')
    h = float(x)
    y = input('What is your weight in kilogram?')
    w = int(y)
    b=w/h
    return b

print(bmi())
