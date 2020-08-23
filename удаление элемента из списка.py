k=int(input("Введите индекс 'k' удаляемого числа в списке (0-48) :"))
k1=k+1
from random import randint
lst=[randint(1,99) for _ in range(50)]
print(lst)
while k<len(lst)-1:
    lst[k]=lst[k1]
    k=k+1
    k1=k1+1
lst.pop()
print(lst)
