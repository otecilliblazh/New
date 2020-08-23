r= int(input("Введите высоту ромба: "))
x=0
c=r//2+1
y=c+1
z=r//2-1
for i in range(c):
    for j in range(r):
        if j==r//2-x or j==r//2+x:
            print("*", end=" ")
        elif r//2-x<j and r//2+x>j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    x=x+1
    print()
for i in range(y,r+1):
    for j in range(r):
        if j==r//2-z or j==r//2+z or j==r//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    z=z-1
    print()
print()