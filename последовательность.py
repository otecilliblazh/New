n=0
s=0
r=0
i=0
c=0
p=0
z=0
a=int(input('Введите целое число:'))
if a==0:
    print("Цикл окончен")
else:
    z=a
    p=a
    i=1
    s=a
    r=a
    k=a%2
    if k!=0:
        n=1
    else:
        c=1
    while True:
        a=int(input("Введите целое число:"))
        if a==0:
            break
        else:
            i=i+1
            s=s+a
            r=s/i
            k=a%2
        if k!=0:
            n=n+1
        else:
            c=c+1
        if a<z:
            z=a
        elif a>p:
            p=a
        else:
            print()
print("Количество введеных чисел:",i)
print("Сумма:",s,"Среднее арифметическое:",r)
print("Максимальное значение:", p,"Минимальное значение:",z)
print("Количество четных чисел:",c,"Количество нечетных чисел:",n)
