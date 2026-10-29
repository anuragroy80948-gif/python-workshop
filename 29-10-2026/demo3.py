#prgrm. for different-different arithmetic operations
print("press 1 for addition")
print("press 2 for sub")
print("press 3 for multiplication")
print("press 4 for division")
ch=int(input("enter your choice"))
a=int(input("enter first no."))
b=int(input("enter second no."))

if(ch==1):
    c=a+b
    print("sum=",c)
if(ch==2):
        c=a-b
        print("sub=",c)
if(ch==3):
        c=a*b
        print("multiplication=",c)
if(ch==4):
        c=a/b
        print("division=",c)