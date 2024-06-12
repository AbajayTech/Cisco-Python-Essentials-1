# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#negative indices
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

#More about the del instruction
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

#The in and not in operators
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#Lists – some simple programs
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

#Now let's find the location of a given element inside a list:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

#how many numbers have you hit in a lottery bet
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

#3.6.6   LAB   Operating with lists ‒ basics

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Remove duplicates by converting the list to a set, then back to a list
my_list = list(set(my_list))

print("The list with unique elements only:")
print(my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []
seen = set()

for number in my_list:
    if number not in seen:
        unique_list.append(number)
        seen.add(number)

my_list = unique_list

print("The list with unique elements only:")
print(my_list)

#3.7. Section 7 – Lists in advanced applications
