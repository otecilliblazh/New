a=int(input("Введите кол-во элементов первого списка:  "))
b=int(input("Введите кол-во элементов второго списка:  "))
from random import randint
lst1=[randint(1,99) for _ in range(a)]
lst1.sort()
print(lst1)
lst2=[randint(1,99) for _ in range(b)]
lst2.sort()
print(lst2)
lst3=[]
i=0
j=0
while i < a and j< b:
    if lst1[i]<lst2[j]:
        lst3.append(lst1[i])
        i=i+1
    else:
        lst3.append(lst2[j])
        j=j+1
while i < a:
    lst3.append(lst1[i])
    i=i+1
while j<b:
    lst3.append(lst2[j])
    j=j+1
print(lst3)
