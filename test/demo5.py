# Function to check whether a number is prime
def prime(number):
	if number < 2:
		return False

	for divisor in range(2, int(number ** 0.5) + 1):
		if number % divisor == 0:
			return False
	return True


number = int(input("Enter a number: "))
if prime(number):
	print(number, "is a prime number")
else:
	print(number, "is not a prime number")
    
