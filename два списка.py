from random import randint
lst=[randint(1,99) for _ in range(50)]
lst1=[randint(1,99) for _ in range(50)]
print(lst)
print(lst1)
print("Количество уникальных чисел в списках - ",len(set(lst))+len(set(lst1)))