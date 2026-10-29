# prg. for palindrome no. checking 
n=int(input("enter any number"))
res=0
temp=n
print("before reverse -",temp)
while(n!=0):
    a=n%10
    res=(res*10)+a
    n=n//10
    if(res==temp):
        print("no. is palindrome")
    else:
        print("not palindrome no.")