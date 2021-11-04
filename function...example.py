import math
def findRoot(a,b,c):
    delta=math.pow(b,2)-(4*a*c)
    if(delta<0):
        print("there is no root")
        return
    else:
        x1=(-b-delta**0.5)/2*a
        x2=(-b+delta**0.5)/2*a
        return (x1,x2)

x=int(input("enter a first coefficient of x"))
y=int(input("enter a second coefficient of x"))
z=int(input("enter a third coefficient of x"))

v=findRoot(x,y,z)
print(v)
