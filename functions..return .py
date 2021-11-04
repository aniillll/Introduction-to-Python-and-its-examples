import math


def factorial(number):
    factoriel = 1
    for i in range(1, number + 1):
        factoriel *= i
    return factoriel


sum: float = 0
x = int(input("enter value of x"))
while True:
    for i in range(1, 7 + 1):
        item =((math.pow(-1, i + 1))*(math.pow(x, i)))/(factorial(i))
        if item >= 0:
            sum = sum + item
    print("results of calculation:", sum)
    break
