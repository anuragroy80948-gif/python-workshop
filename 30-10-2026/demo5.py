n=int(input("enter the number"))
#check for prime number
f=0
for i in range(2,n):
    if(n%i==0):
        f=1
        break
if (f==1):
    print("it is not a prime number")
else:
    print(" it is a prime number")