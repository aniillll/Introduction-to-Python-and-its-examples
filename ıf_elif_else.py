import module1

x = int(input("to make sum enter 1\n to make substruction enter 2\n to make multiplication enter 3\n to make division enter 4"))
while(x==1 or x==2 or x==3 or x==4):

    if(x==1):
        a=int(input("enter number"))
        b=int(input("enter number"))
        print(module1.sum(a,b))
        break
    elif(x==2):
        a=int(input("enter number"))
        b=int(input("enter number"))
        print(module1.subtraction(a,b))

        break
    elif (x == 3):
        a = int(input("enter number"))
        b = int(input("enter number"))
        print(module1.multiplication(a,b))

        break
    elif (x == 4):
        a = int(input("enter number"))
        b = int(input("enter number"))
        print(module1.division(a,b))

        break
    else:
        print("tekrar deneyin")