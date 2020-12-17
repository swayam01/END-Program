# write a python program to substract two numbers and print it
num1 = 1.5
num2 = 6.3
difference = num1 - num2
print(f'Difference: {difference}')

# write a python program to print 5 random integers between 10 and 20
import random
print(random.sample(range(10, 20), 5))

# write a python program to delete a variable
i = 10
del i

# write a python program to perform multiple assignments
a = b = c = 1

# write a python program to swap two numbers
(x, y) = (1, 2)
print(f'Before swapping: x: {x}, y: {y}')
(y, x) = (x, y)
print(f'After swapping: x: {x}, y: {y}')

# write a python program to print bitwise AND operation
a = 60
b = 13
a_and_b = a&b
print(a_and_b)

# write a python program to print bitwise OR operation
a = 60
b = 13
a_or_b = a|b
print(a_or_b)

# write a python program to print bitwise XOR operation
a = 60
b = 13
a_xor_b = a^b
print(a_xor_b)


# write a python program to print binary ones complement on a variable
a = 60
ones_complement_a = ~a
print(ones_complement_a)

# write a python program to print binary left shift on a variable
a = 60
binary_left_shift = a<<2
print(binary_left_shift)

# write a python program to print binary right shift on a variable
a = 60
binary_right_shift = a>>2
print(binary_right_shift)

# write a python function to check if an item exists in a list and return the boolean value
def item_exists(lst, item):
    if item in lst:
        return True
    else:
        return False

# write a python function to get the type of a variable 
def get_type(var):
    return(type(var))

# write a python function to check if an object is an instance of a given class 
def check_instance(derived_class, base_class):
    return(isinstance(derived_class, base_class))

# write a python function to accept user input to continue
def get_userinput():
    while(1):
        do_continue = raw_input('Do you want to continue(y/n)?')
        if do_continue == 'y' or do_continue == 'n':
            return do_continue


# write a python program to create a raw string
str1 = r'hello\n'

# write a python function to print prime numbers between two numbers 
def get_prime_numbers(range1, range2):
    for num in range(range1,range2):
        for i in range(2,num):
            if num%i == 0:
                j=num/i
                break
        else:
            print(num, 'is a prime number')

# write a python function to get the value of maximum integer allowed on the system 
def get_max_integer():
    import sys
    return sys.maxsize

# write a python function to get the absolute value of a number
def get_absolute_value(i):
    return(abs(i))

# write a python function to return the exponential of a number 
def get_exponential_value(i):
    import math
    return(math.exp(i))

# write a python function to return the natural logarithm of a number 
def get_natural_log_value(i):
    import math
    return(math.log(i))

# write a python function to return the base 10 logarithm of a number 
def get_natural_log_value(i):
    import math
    return(math.log10(i))

# write a python function to return the square root of a number 
def get_sqrt(i):
    import math
    return(math.sqrt(i))

# write a python program to print the maximum integer in a list of integers
lst = [10, 20, 30, 40]
print(max(lst))

# write a python program to print the minimum integer in a list of integers
lst = [10, 20, 30, 40]
print(min(lst))

# write a python program to print a random number between 0 and 1
import random
print(random.random())

# write a python program to concatenate two strings and print
str1 = 'hello'
str2 = ' world!'
print(str1 + str2)

# write a python program to print the ascii value of a character
str1 = 'a'
print(ord(str1))

# write a python program to print current date and time 
import datetime
print(datetime.datetime.now())

# write a python program to capitalize a string 
str1 = 'hello'
print(str1.capitalize())

# write a python program to clone a list
a = [1, 2, 3]
b = a[:]

# write a python program to print a list in reverse
a = [1, 2, 3]
print(a[::-1])

# write a python program to print a list in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(sorted(basket))

# write a python function to return union of two sets
def union_set(set1, set2):
    return set1|set2

# write a python function to return union of two sets
def intersection_set(set1, set2):
    return set1&set2

# write a python program to print names of the entries in the directory given by path
path = '/home'
import os
print(os.listdir(path))

# write a python program to create a directory named path
path = 'test'
import os
os.mkdir(path)

# write a python program to add two matrices and print them
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [[X[i][j] + Y[i][j]  for j in range
(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)

# write a python function to check if a string is a palindrome or not
def isPalindrome(s):
    return s == s[::-1]

# write a python program to print the least frequent character in a string
test_str = "this is test string"
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)
print(res)

# write a python program to print sum of elements in a list
lst = range(5)
print(sum(lst))

# write python code to merge two dictionaries
def merge_dict(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
merge_dict(dict1, dict2)
print(dict2)

# write python code to print temperature in celsius to fahrenheit
celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

# write python function to detect if a number is even number
def is_even(num):
    return((num % 2) == 0)

# write python function to detect if a number is odd number
def is_odd(num):
    return((num % 2) != 0)

# write python function to detect if an year is leap year
def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True 
            else:
                return False
        else:
            return True 
    else:
        return False 

# write a python program to print the largest number among the three input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

# write a python program to find the factorial of a number provided by the user.
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

# write a python program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

# write a python program to print transpose a matrix and print
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


# write a python program to convert Kilometers to Miles
kilometers = float(input("Enter value in kilometers: "))

conv_fac = 0.621371

miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

# write a python program to check if a number is positive, negative or 0
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

# write a python program to check if a number is a prime number
num = int(input("Enter a number: "))

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")

# write a python function to find H.C.F of two numbers
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

# write a python python program to find the L.C.M. of two input number
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))

# write a python function to find the factors of a number
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# write a python program to remove punctuations from a string and print it
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string: ")

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)

# write a python program to count the number of each vowel and print them
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


# write a python program to print week number from a date
import datetime
print(datetime.date(2015, 6, 16).isocalendar()[1])

from datetime import date, timedelta

def all_sundays(year):
       dt = date(year, 1, 1)
       dt += timedelta(days = 6 - dt.weekday())
       while dt.year == year:
          yield dt
          dt += timedelta(days = 7)

for s in all_sundays(2020):
    print(s)

# Write a Python program to get the last day of a specified year and month.
import calendar
year = 2020
month = 12 
print(calendar.monthrange(year, month)[1])

# Write a Python program to convert a string to datetime.
from datetime import datetime
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)

# Write a Python program to subtract five days from current date
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)

# Write a Python program to convert Year/Month/Day to Day of Year.
import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)
