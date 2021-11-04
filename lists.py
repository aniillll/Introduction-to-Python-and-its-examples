list=[]
def datainpu():
    a = int(input("enter your age"))
    b = str(input("enter your name"))
    c = str(input("enter your surname"))
    d = float(input("enter your general point average"))
    global list
    list= [a, b, c, d]

datainpu()
print(list)
