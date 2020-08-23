a=int(input("Введите год :"))
b=a%4
c=a%400
d=a%100
if d==0 and c!= 0:
    print("No")
elif b == 0:
    print("Yes")
else:
    print("No")

