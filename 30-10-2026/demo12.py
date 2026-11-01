a=int(input("enter the num:"))
b=0
for i in range(a+1,1,-1):
    for j in range(i,1,-1):
        b=b+1
        print(b, end=" ")
    print()
