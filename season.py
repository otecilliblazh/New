def season():
    a=int(input('Введите месяц (1-12):  '))
    if a==12 or a==1 or a==2:
        b='Зима'
        return b
    elif a>2 and a<6:
        b="Весна"
        return b
    elif a>5 and a<9:
        b='Лето'
        return b
    else:
        b='Осень'
        return b
r=season()
print(r)