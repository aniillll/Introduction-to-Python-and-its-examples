# vize final,quiz1,quiz2 quiz3 notunu alıcaz ve harf notunu vericez

midtherm=float(input("enter your midtherm grade"))
final=float(input("enter your final grade"))
q1=float(input("enter your quiz 1 grade"))
q2=float(input("enter your quiz 2 grade"))
q3=float(input("enter your quiz 3 grade"))

average=(float(q1)+float(q2)+float(q3)+float(midtherm)+float(final))/5
print(average)

if average>=85:
    print("you get AA note")

elif average>=70:
    print("you get BA note")

elif average>=60:
    print("you get CB note")
elif average>=50:
    print("you get CC note")
elif average>=40:
    print("you get DC note")

else:
    print("DD ALDINIZ KALDINIZ")