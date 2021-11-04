defusername="anil"
defpassword="1245"

while(True):
  user_name=str(input("enter user name"))
  password=str(input("enter your password"))
  if (password==defpassword) and (defusername==user_name):
      print("hoş geldiniz",user_name)
      break
  elif((password!=defpassword) and (defusername==user_name)):
      print("kullanıcı adınız yanış,tekrar deneyin")
  elif ((password!=defpassword) and (defusername==user_name)):
      print("şifreniz adınız yanış")
      print("şifrenizi değiştirmek ister misiniz(E/H)")
      answer=str(input("enter your choose"))
      if(answer=='E'):
           new_password: str=str(input("enter your new password"))
           defpassword=new_password
           print("şifre başarı ile değiştirildi")

  else:
      print("tekrar deneyin")





