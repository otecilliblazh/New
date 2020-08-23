
r=int(input("Введите высоту  :"))
c=r*2-1
x=0
for i in range(r):
    for j in range(c):
        if j==c//2-x or j==c//2+x or i==r-1:
            print("*", end=" ")
        elif c//2-x<j and c//2+x>j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    x=x+1
    print()
print()

