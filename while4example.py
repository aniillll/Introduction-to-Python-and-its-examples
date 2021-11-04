import math
i=0
decimal=0

number=int(input("enter a binary number"))
original_number=number
while (True):

    if (number!=0):
        remainder = int((number) % (10))
        if ((remainder==1) or (remainder==0)):
            i+=1
            number=int(number/10)
    else:
        break
print("i equal to",i)

j=0
remainder=0
while(j<i):
    remainder=(original_number%10)
    decimal += int(remainder * math.pow(2, j))
    original_number=int(original_number/10)
    j+=1
print("solution:",decimal)


