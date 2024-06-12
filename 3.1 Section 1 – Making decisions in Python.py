var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)

var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

#centigrade_outside >= 0.0  # Greater than or equal to
#current_velocity_mph < 85  # Less than
#current_velocity_mph <= 85  # Less than or equal to

n = int(input("Enter a number: "))
print(n >= 100)

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)


#LAB Comparison operators and conditional execution
input_str = input("Enter a plant name: ")

if input_str == "Spathiphyllum":
  print("Yes - Spathiphyllum is the best plant ever!")
elif input_str == "spathiphyllum":
  print("No, I want a big Spathiphyllum!")
else:
  print(f"Spathiphyllum! Not {input_str}!")

#LAB Essentials of the if - else statement
income = float(input("Enter the annual income: "))

if income <= 85528:
  tax = income * 0.18 - 556.02
else:
  # Income exceeding the threshold
  surplus = income - 85528  # Calculate the amount exceeding the threshold
  tax = 14839.02 + surplus * 0.32  # Base tax + tax on surplus

# Ensure tax is non-negative (no refunds)
tax = max(tax, 0.0)  # Set tax to 0 if negative

# Round and print the tax
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#LAB Essentials of the if - elif - else statement
year = int(input("Enter a year: "))

if year < 1582:
  print("Not within the Gregorian calendar period")
else:
  # Leap year logic using nested if-elif-else
  if year % 4 != 0:
    print("Common year")
  elif year % 100 != 0:
    print("Leap year")
  elif year % 400 != 0:
    print("Common year")
  else:
    print("Leap year")





