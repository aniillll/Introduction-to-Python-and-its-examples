def Geometric_shape_modula(shape):
    if len(shape)==3:
        a=shape[0]
        b=shape[1]
        c=shape[2]
        if (a+b)>c and (c+b)>a and (a+c)>b :
            if(a==b and b==c and a==c):
                print("eşkenar ücgen")
            elif((a==b and (b!=c or a!=c)) or (a==c and (b!=c or a!=b)) or (c==b and (b!=a or a!=c))):
                print("ikiz kenar ücgen")
            else:
                print("çeşitkenar ücgen")
        else:
            print("ücgen belirtmiyor")

    elif len(shape) == 4:
        a = shape[0]
        b = shape[1]
        c = shape[2]
        d = shape[3]
    else:
        return

control: int=0
i=0
j=0
x=[]
while(control!=-1):
    control= int(input("enter edge number out of enter -1"))
    if(control==3):
            a=int(input("enter edge length"))
            b = int(input("enter edge length"))
            c = int(input("enter edge length"))
            x=[a,b,c]
            Geometric_shape_modula(x)
            control = int(input("enter edge number out of enter -1"))
    elif(control==4):
            a =int(input("enter edge length"))
            b = int(input("enter edge length"))
            c =int(input("enter edge length"))
            d = int(input("enter edge length"))
            x = [a, b, c,d]
            Geometric_shape_modula(x)
            control = int(input("enter edge number out of enter -1"))
    else:
            break