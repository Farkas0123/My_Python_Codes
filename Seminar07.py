import random

# Assignment/exercise 1 (10 minutes)
# Given N pieces of temperature values (real numbers) in degrees Celsius. Let's convert them
# to Fahrenheit, then display both the original and the new values on the screen!
t = [21, 22, 23]
t_f = []
for i in range(len(t)):
    t_f.append(t[i]*(9/5)+32)
print(t)
print(t_f)


# Assignment/exercise 2 (10 minutes)
# Given the exam result of N students (integers between 0 and M). A score of at least 50% is
# required to pass the exam. Let's select and display the scores of the students who passed
# the exam!

M = 100
N = 5
results = [0]*N
passed = {}
for i in range(N):
    results[i] = random.randint(1, 100)
    if results[i] >= 50:
        passed[i] = results[i]
print(results)
print(passed)

# Assignment/exercise 3 (10 minutes)
# A dice is rolled N times, and the values of the rolls are stored in a list. Separate even and
# odd values into two particular lists.

N = 10
numbers = [0]*N
odd = []
even = []
for i in range(N):
    numbers[i] = random.randint(1,6)
    if numbers[i] % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
print(numbers)
print(even)
print(odd)

# Assignment/exercise 4 (10 minutes)
# Generate 5 random numbers between 0 and N, then sort them in ascending order 
# the swap sort algorithm.
# • Display each step when a swap is made
N = 100
numbers = [0]*5
m = len(numbers)
for i in range(m):
    numbers[i] = random.randint(0,N)
print(numbers)
for i in range(m-1):
    for j in range(i+1, m):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            print(numbers)

# Assignment/exercise 5 (10 minutes)
# Given N float numbers between a and b. Sort them in descending order using the maximum
# selection sort algorithm.
# • Display each step when a swap is made

N = 5
numbers = [0]*N
for i in range(N):
    numbers[i] = random.randint(3, 1000)
print('------------------')
print(numbers)
for i in range(N-1):
    max = i
    for j in range(i+1, N):
        if numbers[j] > numbers[max]:
            max = j
    numbers[i], numbers[max] = numbers[max], numbers[i]
    print(numbers)

# Assignment/exercise 6 (10 minutes)
# Given a sentence with lowercase letters. Sort its letter in ascending order alphabetically
# using the bubble sort algorithm.
    
print('__________________________')
sentence = 'this is my sentence which I would like to sort in no time'
ls = list(sentence.lower())
for i in range(len(ls)-1,0,-1):
    for j in range(i):
        if ls[j] == ' ': ls.pop(j)
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
ordered = ''.join(ls)
print(ordered)
print()
    
# Homework:
# We have a list of N names. Select the ones that are shorter than the average length into a
# new list.
    
names = ['asdfasdf','asds','as']
shorter= []
summa = 0
for i in range(len(names)):
    summa += len(names[i])
avg = summa/len(names)

for i in range(len(names)):
    if len(names[i])<avg:
        shorter.append(names[i])
print(shorter)


#_______________________________________________________________________________________________________________


# Assignment/exercise 1 (20 minutes)
# Write a function to check if a number N is prime!
# • find the divisors from 2 up to √𝑁
# • use this function to display the prime numbers between 1 and 100
# • Optionally: use another primality test, such as Fermat method. In case of
# Fermat method, try it with a pseudoprime too, e.g. 341

def is_prime(n):
    divisor= 2
    if n == 1: return False
    while divisor <= n**0.5 and n % divisor != 0:
        divisor += 1
    if divisor > n**0.5:
        return True
    else:
        return False
for i in range(1, 100):
    if is_prime(i):
        print(i, end = ' ')


# Assignment/exercise 2 (20 minutes)
# Write a procedure to display the first N Fibonacci numbers!
# • N should be a mandatory parameter
# • The zeroth and the first elements should be optional parameters with a
# default value of 1
# • Use the following formula to calculate the nth Fibonacci number:
# Fn=Fn−1+Fn−2 (n >1)
print()
def Fibonacci(n):
    list = [1,1]
    for i in range (2,n+2):
        list.append(list[i-1]+list[i-2])
    return list
print(Fibonacci(10))

# Assignment/exercise 3 (30 minutes)
# Write a function to calculate the factorial for the number n. Using this to ...
# • create a new function to calculate the binomial coefficient according to the
# following formula: nCr = n!/(r! * (n-r)!)
# • create a procedure to display the first N rows of the Pascal’s triangle
def factorial(n):
    prod = 1
    for i in range(n):
        prod = prod * (i+1)
    return prod

def bino(n, r):
    return (factorial(n))/(factorial(r)*factorial(n-r))

def pas(n):
    line = []
    for i in range(n+1):
        line.append(bino(n,i))
    return line

for i in range(10):
    print(pas(i))
# Assignment/exercise 4 (20 minutes)
# Write a program that is divided into three logical parts:
# • the first part generates n random integers between a and b, and puts them
# into a list
# • the second part sorts the list elements in ascending order (you can use any
# learned sorting algorithm)
# • the third part displays the original and the sorted lists
# • Use functions and/or procedures to solve this exercise. Ask the values of n,
# a and b from the user.
print('_____________________________')
def generate(n,a,b):
    list = []
    for i in range(n):
        list.append(random.randint(a,b))
    return list

def sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

n = int(input('n = '))
a = int(input('a = '))
b = int(input('b = '))

rlist = generate(n,a,b)
print(rlist)
olist = sort(rlist)
print(olist)
print('_______________________')
# Assignment/exercise 5 (20 minutes)
# Write a function that returns a dictionary containing the frequency of characters of a text
# received as a parameter.
# • e.g., if the text is: “Hello World”,
# • result should be: {H: 1, e: 1, l: 3, o: 2, W: 1, r: 1, d: 1 }
# • double each value in the dictionary using map and lambda functions!
# • filter the dictionary using filter and lambda functions by keeping only those
# key-value pairs when the value is divisible by 3






# Assignment/exercise 6 (30 minutes)
# Write a module that implements basic operations on three-dimensional vectors using
# functions
# • to be implemented: addition, subtraction, multiplication by a number, dot
# product
# • write a program that imports this module and performs some vector
# operations (at least one of each type)


# Homework:
# Write a Python function to check whether a number is palindromic or not. (A palindromic
# number is a number (such as 121) that remains the same when its digits are reversed)
# • using this function display all palindromic number between 1 and 500

def palindromic(a,b):
    list = []
    for i in range(a,b):
        if str(i)[0]==str(i)[-1]:
            list.append(i)
    return list
print(palindromic(1,500))