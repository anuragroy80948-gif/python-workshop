#multiple of any digit number by for loop
# n=int(input("enter your number"))

# for i in range(1,11):
#     print(n," * ",i,"=",n*i)

n = int(input("Enter number "))
a=0
while(a<n):
    a += 3
    print(a, end=" ")