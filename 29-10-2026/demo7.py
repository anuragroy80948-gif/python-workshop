#prg. for check armstrong no.
n=int(input("enter any no."))
r=n
res=0
temp=n
while(n!=0):
    a=n%10
    res=(a**3)+res
    n=n//10
if(res==temp):
        print(r,"no. is armstrong")
else:
        print(r,"not armstrong no.")