# reverse of any digit no. 
n=int(input("enter any number"))
res=0
temp=n
print("before reverse -",temp)
while(n!=0):
    a=n%10
    res=(res*10)+a
    n=n//10
print("after reverse -",res)