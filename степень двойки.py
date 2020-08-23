a=(int(input("Введите число:")))
b=1
c=2
while a>c or a==c:
    c=c*2
    b=b+1
c=int(c/2)
b=b-1
print(a,b,c,"  2 *",b,"=",c,sep=" ")