#The while loop
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

#Using a counter variable to exit a loop
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#3.2.4   LAB   Guess the secret number
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!  |
| Enter an integer number    |
| and guess what number I've   |
| picked for you.        |
| So, what is the secret number? |
+================================+
""", end=""  # Prevent adding a newline after the intro text
)

while True:
  try:
    guess = int(input(": "))  # Take input after the intro text
    if guess == secret_number:
      print(guess)
      print("Well done, muggle! You are free now.")
      break  # Exit the loop if the guess is correct
    else:
      print("Ha ha! You're stuck in my loop!")
  except ValueError:
    print("Invalid input. Please enter an integer.")

#3.2.5 Looping your code with for
for i in range(10):
    print("The value of i is currently", i)

for i in range(2, 8): print("The value of i is currently", i)

for i in range(2, 8, 3):
    print("The value of i is currently", i)

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

#3.2.7 LAB Essentials of the for loop – counting mississippily
import time
# Loop to count mississippily
for i in range(1, 6):  # Range 1 to 6 to print numbers 1 to 5
  print(i, "Mississippi")
  time.sleep(1)  # Pause for one second

# Print the final message
print("Ready or not, here I come!")

#3.2.8 The break and continue statements
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

#The break variant
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

#the continue variant:
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

#3.2.9   LAB   The break statement – Stuck in a loop
secret_word="chupacabra"
while True:
  try:
    guess = str(input(" Enter Secret Word: "))  # Take input
    if guess == secret_word:
      print("You've successfully left the loop.")
      break  # Exit the loop if the guess is correct
    else:
      print("Ha ha! You're stuck in my loop!")
  except ValueError:
    print("Invalid input. Please enter a word.")

#3.2.10   LAB   The continue statement – the Ugly Vowel Eater
user_word = input("Enter a word: ")
user_word = user_word.upper()  # Convert the word to uppercase

vowels = "AEIOU"  # Define the vowels to eat

# Loop through each letter in the word
for letter in user_word:
  # Skip vowels using the continue statement
  if letter in vowels:
    continue

  # Print the remaining consonants
  print(letter)

#3.2.11   LAB   The continue statement – the Pretty Vowel Eater
word_without_vowels = ""  # Initialize an empty string to store consonants

user_word = input("Enter a word: ")
user_word = user_word.upper()  # Convert the word to uppercase

vowels = "AEIOU"  # Define the vowels to eat

# Loop through each letter in the word
for letter in user_word:
  # Conditionally add consonants to the word_without_vowels string
  if letter not in vowels:
    word_without_vowels += letter  # Concatenate consonants

# Print the word without vowels
print(word_without_vowels)

#3.2.14   LAB   Essentials of the while loop
blocks = int(input("Enter the number of blocks: "))

# Initialize variables
height = 0
layer_blocks = 1  # Start with 1 block in the first layer

# Build the pyramid layer by layer
while blocks >= layer_blocks:
  blocks -= layer_blocks  # Subtract blocks used for the current layer
  height += 1  # Increment height for a completed layer
  layer_blocks += 1  # Increase the number of blocks needed for the next layer

# Print the result
print("The height of the pyramid:", height)

#3.2.15   LAB   Collatz's hypothesis
def collatz_conjecture(number):
  """
  This function checks the Collatz conjecture for a given number.

  Args:
      number: The natural number to start with.

  Returns:
      A tuple containing the list of intermediate values and the number of steps taken.
  """
  steps = 0
  collatz_sequence = [number]
  while number != 1:
    if number % 2 == 0:
      number //= 2  # Integer division for efficiency
    else:
      number = 3 * number + 1
    steps += 1
    collatz_sequence.append(number)
  return collatz_sequence, steps

# Get user input
number = int(input("Enter a natural number: "))

# Check the Collatz conjecture for the number
collatz_sequence, steps = collatz_conjecture(number)

# Print the results
print("Collatz Sequence:", collatz_sequence)
print("Steps taken:", steps)



