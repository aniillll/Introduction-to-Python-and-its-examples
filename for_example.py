defuser:str="anil"
defpassword:int=1345

while(True):
    user=str(input("enter a user name"))
    password=int(input("enter a password"))
    if((defpassword!=password) or (defuser!=user)):
        print("try again")
    else:
        print("hoş geldiniz")
        break

#listedeki her bir elemanı i ye atıyor ve i arttıkça diğerbir elemana eşitleniyor i ve printle sırayla bastırıoruz
list=[int(input("enter a number")),int(input("enterumber")),int(input("enter a number")),int(input("enter a number"))]
print(list)
for i in range(1,10):
    if list in range(1,10):
        continue
    else:
        print(i)


