#find max among 3 no.s using ladder if
a=int(input("enter first no."))
b=int(input("enter second no."))
c=int(input("enter third no."))
if(a>b and a>c):
    print(a," is max")
elif(b>c):
    print(b," is max")
else:
    print(c," is max")