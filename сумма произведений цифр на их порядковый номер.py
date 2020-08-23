a=list(input ('Введите целое многозначное число: '))
for id,item in enumerate(a):
    a[id]=int(a[id])*(id+1)
a=sum(a)
print(a)