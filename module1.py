
def sum(x="atanmamış değer",y="atanmamış değer"):
    sum=0
    if(x!="atanmamış değer" and y=="atanmamış değer"):
          sum=sum+x
          return sum
    else:
          sum=sum+x+y
          return sum

def subtraction(x="atanmamış değer",y="atanmamış değer"):
    if(x!="atanmamış değer" and y=="atanmamış değer"):
        substraction=0
        substraction = x-substraction
        return substraction
    else:
        substraction = 0
        substraction=x-y
        return substraction
def multiplication(x,y):
    if(x!="atanmamış değer" and y=="atanmamış değer"):
        multiply=1
        multiply = multiply*x
        return  multiply
    else:
        multiply=1
        multiply = multiply*x*y
        return multiply
def division(x,y):
    if(x!="atanmamış değer" and y=="atanmamış değer"):
        division=0
        division = division/x
        return  division
    else:
        division=x/y
        return division