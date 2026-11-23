#midddle value
a=10
b=5
c=7

middle = sorted((a, b, c))[1]
if (a <= b <= c) or (c <= b <= a):
	middle = b
elif (b <= a <= c) or (c <= a <= b):
	middle = a
else:
	middle = c

print("Middle value:", middle)