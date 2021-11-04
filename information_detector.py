import time
def check_card_number(card_numberx):

    while (card_numberx != 123932232342):
       number=int(input("enter your card number"))
       if(card_numberx == number):
           break

    print("well come to yapı kredi bank,Anil!")

def check_password(pasword_number):
    while(pasword_number !="anil2421"):
        print("your password is not correct")
        new_password=str(input("enter your password"))
        if(pasword_number==new_password):
            break
    print("your password is correct")

def making_process(choosen):
    if(choosen==1):
        cekilecek_para=int(input("lütfen çekmek istediğiniz parayı yazın"))
        time.sleep(10)
        print("paranız çekiliyor..")
        time.sleep(10)

    else:
        yatırılacak_para=int(input("lütfen yatırmak istediğiniz parayı yazın"))
        time.sleep(10)
        print("paranız yatırılıyor..")
        time.sleep(10)
    print("işlem tamamlandı")

card_number1=int(123932232342)
check_card_number(card_number1)
password=str(input("enter your pasword"))
check_password(password)
print("Para çekmek için 1 yazın","\n","para yatırmak için 2 yazın","\n")
choose=int(input("please choose make your process"))
making_process(choose)
