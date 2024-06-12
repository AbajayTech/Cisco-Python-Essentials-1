numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list contents:", numbers)  # Printing previous list contents.

print("\nList length:", len(numbers))  # Printing the list's length.
###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###
numbers = [111, 7, 2, 1]
print(numbers[-1])

#3.4.6 LAB The basics of lists
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# Step 1: Prompt user to replace the middle number
new_number = int(input("Enter a number to replace the middle number in the list: "))
hat_list[2] = new_number

# Step 2: Remove the last element from the list
hat_list.pop()

# Step 3: Print the length of the list
print("Length of the hat_list:", len(hat_list))

print(hat_list)

#Method invocation : result = data.method(arg)

#A new element may be glued to the end of the existing list: list.append(value)

#The insert() method is a bit smarter ‒ it can add a new element at any place in the list, not only at the end.
#list.insert(location, value)

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)
numbers.insert(1,333)
print(numbers)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

#Lists in action
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

#3.4.11   LAB   The basics of lists ‒ the Beatles
# Step 1: Create an empty list named beatles
beatles = []

# Step 2: Add John Lennon, Paul McCartney, and George Harrison to the list
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Step 3: Prompt the user to add Stu Sutcliffe and Pete Best to the list
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(member)

# Step 4: Remove Stu Sutcliffe and Pete Best from the list
del beatles[3:5]

# Step 5: Add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")

# Print the updated list
print("Current members of the Beatles:")
for member in beatles:
    print(member)


# testing list legth
print("The Fab", len(beatles))


