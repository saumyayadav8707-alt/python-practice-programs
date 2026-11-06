# Basic Python Practice Programs - Semester 1
# Author: Saumya Yadav

# 1. Program to calculate sum and average of numbers in a list
marks = [78, 85, 69, 92, 74]
total = sum(marks)
average = total / len(marks)
print("Marks List:", marks)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("-" * 40)

# 2. Program to check whether a number is Even or Odd
num = 24
if num % 2 == 0:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")
print("-" * 40)

# 3. Program to find the factorial of a number using a loop
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial of", n, "is:", factorial)
print("-" * 40)

# 4. Program to count vowels in a string
text = "Data Science and Machine Learning"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Sample Text:", text)
print("Number of vowels:", count)
