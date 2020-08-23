k=int(input("Введите индекс 'k' добавляемого числа в списке (0-48): "))
c=int(input("Введите значение 'С' добавляемого числа в списке : "))
from random import randint
lst=[randint(1,99) for _ in range(50)]
print(lst)
k1=len(lst)
k2=k1-1
lst.append(10)
while k<k1 :
    lst[k1]=lst[k2]
    k1=k1-1
    k2=k2-1
lst[k]=c
print(lst)

