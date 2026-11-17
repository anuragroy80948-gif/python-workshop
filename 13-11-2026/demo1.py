#Grade calculator

name = input("Enter your name: ")
P=int(input("Enter physics marks: "))
C=int(input("Enter chemistry marks: "))
M=int(input("Enter maths marks: "))
TOTAL = P + C + M
Grade=0
percentage = TOTAL / 3

if percentage >= 90 and percentage <= 100:
    Grade = "A"

elif percentage >= 80 and percentage < 90:
    Grade = "B"

elif percentage >= 70 and percentage < 80:
    Grade = "C"

elif percentage >= 60 and percentage < 70:
    Grade = "D"

else:
    Grade = "F"

print(f"Student: {name}")
print(f"Physics: {P}")
print(f"Chemistry: {C}")
print(f"Maths: {M}")
print(f"Total Marks: {TOTAL}")
print(f"Percentage: {percentage}")
print(f"Grade: {Grade}")