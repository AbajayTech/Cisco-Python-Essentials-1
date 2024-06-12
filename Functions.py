def message():
    print("Enter a value: ")

print("We start here.")
message()
print("We end here.")

def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function


#4.3.4 LAB A leap year: writing your own functions
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
test_data = [1900, 2000, 2015, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#4.3.5 LAB How many days: writing and using your own functions
def is_year_leap(year):
    # A year is a leap year if it is divisible by 4,
    # except for years that are divisible by 100,
    # but including years that are divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    # Check if the input month is valid
    if month < 1 or month > 12:
        return None

    # List of days in each month for a non-leap year
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust February for leap years
    if month == 2 and is_year_leap(year):
        return 29

    return month_days[month - 1]


test_years = [1900, 2000, 2015, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#4.3.6   LAB   Day of the year: writing and using your own functions
def is_year_leap(year):
    # A year is a leap year if it is divisible by 4,
    # except for years that are divisible by 100,
    # but including years that are divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    # Check if the input month is valid
    if month < 1 or month > 12:
        return None

    # List of days in each month for a non-leap year
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust February for leap years
    if month == 2 and is_year_leap(year):
        return 29

    return month_days[month - 1]


def day_of_year(year, month, day):
    # Check if the month is valid
    if month < 1 or month > 12:
        return None

    # Get the number of days in the given month
    days_in_this_month = days_in_month(year, month)

    # Check if the day is valid
    if day < 1 or day > days_in_this_month:
        return None

    # Calculate the day of the year
    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month(year, m)
    day_of_year += day

    return day_of_year


# Test cases
print(day_of_year(2000, 12, 31))  # Should return 366 (leap year)
print(day_of_year(2020, 2, 29))  # Should return 60 (leap year)
print(day_of_year(2019, 2, 28))  # Should return 59 (non-leap year)
print(day_of_year(2021, 1, 1))  # Should return 1
print(day_of_year(2021, 4, 30))  # Should return 120

# Additional test cases
print(day_of_year(2000, 2, 30))  # Invalid day for February in a leap year
print(day_of_year(2019, 2, 29))  # Invalid day for February in a non-leap year
print(day_of_year(2021, 13, 1))  # Invalid month
print(day_of_year(2021, 0, 1))  # Invalid month
print(day_of_year(2021, 6, 31))  # Invalid day for June

# More comprehensive tests
test_years = [1900, 2000, 2016, 1987, 2020, 2021, 2022, 2023]
test_months = [2, 2, 1, 11, 2, 1, 12, 12]
test_days = [28, 29, 31, 30, 29, 1, 31, 30]
expected_results = [59, 60, 31, 334, 60, 1, 365, 364]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    day = test_days[i]
    print(yr, mo, day, "->", end="")
    result = day_of_year(yr, mo, day)
    if result == expected_results[i]:
        print("OK")
    else:
        print("Failed")

#4.3.7   LAB   Prime numbers ‒ how to find them
def is_prime(num):
    # A prime number is greater than 1
    if num <= 1:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Testing the is_prime function
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#4.3.8   LAB   Converting fuel consumption
def liters_100km_to_miles_gallon(liters):
    miles_per_km = 1609.344 / 1000  # Convert meters to kilometers
    gallons_per_liter = 3.785411784
    mpg = (100 * miles_per_km) / (liters * gallons_per_liter)
    return mpg

def miles_gallon_to_liters_100km(miles):
    km_per_mile = 1.609344  # Convert miles to kilometers
    liters_per_gallon = 3.785411784
    l_per_100km = (100 * liters_per_gallon) / (miles * km_per_mile)
    return l_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


#4.4. Section 4 – Scopes in Python
#4.4.2 Functions and scopes: the global keyword
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

#4.5.1 Sample functions: Evaluating the BMI
def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2
print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))

#4.5.2 Sample functions: Triangles
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

#Triangles and the Pythagorean theorem
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')

#The hypotenuse is the longest side
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

#Evaluating a triangle's area
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))

#4.5.3 Sample functions: Factorials
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # testing
    print(n, factorial_function(n))

#4.5.4 Fibonacci numbers
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))

#4.5.5 Recursion(technique where a function invokes itself.)
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))





