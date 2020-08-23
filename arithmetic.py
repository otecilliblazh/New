def arithmetic():
    arg1=float(input('Введите первый аргумент: '))
    arg2=float(input('Введите второй аргумент: '))
    arg3=str(input('Введите операцию: '))
    if arg3=='+':
        res = arg1+arg2
        print(res)
        return res
    elif arg3=='-':
        res = arg1-arg2
        print(res)
        return res
    elif arg3=='*':
        res = arg1*arg2
        print(res)
        return res
    elif arg3=='/':
        res = arg1/arg2
        print(res)
        return res
    else:
        print('Неизвестная операция')
arithmetic()
