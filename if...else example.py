"""
Burada öğrencilerin notlarını alıp ona göre geçip geçemediğine karar vericez
"""
midtherm = float(input("enter midtherm note"))
final = float(input("enter final note"))
lab = float(input("enter lab note"))

Total_grade=((20*midtherm)+(40*final)+(40*lab))/100
print(Total_grade)

if Total_grade>60:
    print("you pass class")

else:
    print("you dont pass class")
