from random import randint
lst=[randint(1,99) for _ in range(50)]
print(lst)
print("Количество разичных чисел в списке - ",len(set(lst)))