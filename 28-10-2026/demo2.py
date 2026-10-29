#and /or operator
prev =int(input("enter your percentage"))
yrs =int(input("enter your passing year"))
res= (prev>=75 and yrs==2028)
res= (prev>=70 or yrs==2028)
res= not(prev>=65 and yrs==2028)
res= not(prev>=60 or yrs==2028)
print(res)