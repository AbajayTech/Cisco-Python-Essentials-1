print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")



#Type casting (type conversions)

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

#String operators
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#Type conversions once again
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

#   LAB   Simple input and output
# Get user input for numbers
a = float(input("Enter a float value for variable a: "))
b = float(input("Enter a float value for variable b: "))

# Perform arithmetic operations
sum = a + b
difference = a - b
product = a * b
quotient = a / b

# Print the results
print("The sum of", a, "and", b, "is", sum)
print("The difference of", a, "and", b, "is", difference)
print("The product of", a, "and", b, "is", product)
print("The quotient of", a, "and", b, "is", quotient)

print("\nThat's all, folks!")

#LAB Operators and expressions
x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

#LAB Operators and expressions – 2
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

num_1 = input("Enter the first number: ")  # Enter 12
num_2 = input("Enter the second number: ")  # Enter 21

print(num_1 + num_2)  # the program returns 1221

my_input = input("Enter something: ")  # Example input: hello
print(my_input * 3)  # Expected output: hellohellohello

x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")

x = input("Enter a number: ") # The user enters 2
print(type(x))


