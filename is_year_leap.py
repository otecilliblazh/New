def is_year_leap():
    a=int(input('Введите год:  '))
    if a%400==0:
        return True
    elif a%4!=0 or a%100==0:
        return False
    else:
        return True
r=is_year_leap()
print(r)