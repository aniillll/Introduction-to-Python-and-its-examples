import math

x: float = float(input("enter value of x"))

if x < -3:
    result: float = (math.pow(x, 3) + 4) / (math.pow(x, 2))
    print(result)
elif -2 < x < 0:
    islem=math.pow(x,2)+(3*x)-10
    sonuc=math.fabs(islem)
    print(sonuc)
else:
    calculate=math.pow(x,2)-4
    print(calculate)