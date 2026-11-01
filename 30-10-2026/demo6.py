#prg for fibonacci series
a=int(input("enter the value"))
b=0
c=1
print(b,c)
for i in range(1,a+1):
    d=b+c
    print(d)
    b=c
    c=d
    