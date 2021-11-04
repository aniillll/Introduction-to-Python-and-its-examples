import math

#a=5
#b=3
#c=2
#d=10

#result=(math.pow(a,3)+math.pow(b,2)+math.pow(c,1))/d

#print(result)

#print("python programming course will be funny\n")
#print("python programming course\n will be funny\n")
#print("python\nprogramming\ncourse\nwill\nbe\nfunny")

#a=input("enter first integer")
#b=input("enter first integer")
#c=input("enter first integer")
#d=input("enter name")

#print(str(d))
#sum1=int(a)+int(b)+int(c)
#sum2=int(a)+int(b)
#sum2=int(sum2)+int(c)
#sum3=int(a)
#sum3=int(sum3)+int(b)+int(c)
#print(int(sum3))
#print(int(sum1))
#print(int(sum2))


x: float=input('enter integer number')
result1:float= (float(45) + (float(x) + float(4))) / float(8)
print("first solution:\n",result1)

solution=  (((float(x) * float(x) )+ (float(3) * float(x)) - 10)/(float(8)*float(x)*float(x)-float(24)))
print("second solution:\n",solution)

result2:float=((math.pow(float(x),2)-20)/((3*float(x))+(2))+(float(x)-1)/(6))
print("third solution:\n",result2)

result3:float=(math.pow(float(x),3)*(float(x)+1))/(math.pow((float(x)-1),2))
print("fourth solution:\n",result3)

