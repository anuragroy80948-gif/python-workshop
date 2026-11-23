"""Calculate 1! + 2! + ... + n!."""

n = int(input("Enter n: "))
factorial = 1
total = 0

for number in range(1, n + 1):
	factorial *= number
	total += factorial

print(total)
