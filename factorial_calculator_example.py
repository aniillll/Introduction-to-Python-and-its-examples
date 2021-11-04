import math
sum:float=0
factorial=1
x=int(input("enter value of x"))
while True:
    for i in range(1,7+1,1):
        factorial=factorial*i
        item=(math.pow(-1,i+1))*(math.pow(x,i))/(factorial)
        if item >= 0:
            sum=sum+item
    print("results of calculation:",sum)
    break

