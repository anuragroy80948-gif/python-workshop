#check for LEAP YEAR
a=int(input("enter the value"))

#checking for conditions
if(a%4==0):
    print(a," is a leap year")
elif(a%400==0):
    print(a," is a leap year")
else:
    print(a," is a not leap year")