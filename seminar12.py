# Short exercises - use only algorithmic structures if possible
#1.  Write a short program or a function which returns the number of digits of a given whole number!
# for example: 
# x = 5436 --> output: 4
 
def numlen(x):
    strx = str(x)
    count = 0
    for i in strx:
        count += 1
    return count
print(numlen(123456789))

#2 Write a short program or a function that replace all uppercase letters in a string with lowercase leters and vice versa.
# for example:
# s = "Hello World" --> output: hELLO wORLD
def bigsmall(s):
    result = ""
    for i in s:
        if i.upper() != i:
            result = result + i.upper()
        elif i.upper() == i:
            result = result + i.lower()
        else:
            result = result + i
    return result
print(bigsmall('Hello World'))

 
#3 Write a short program or a function that removes all occurrence of a specific item in a list
# for example:
# item = 4
# l = [4, 5, 3, 3, 2, 4, 1] output: [5, 3, 3, 2, 1]
 
#4 We have a dictionary. Write a short program or a function which returns if a key is present in the dictionary.
# for example:
# key = "country"
# d = {'name': 'Jessica', 'country': 'UK', 'phone': 1111} --> output: True
 
#5 We have a tuple. Write a short program of a function which returns the number of occurence of a given number.
# for example:
# num = 8
# t = (3, 4, 4, 8, 1, 11, 8) --> output: 2
 
# Longer exercises based on grades.csv file
#1. Create a function which decides whether a student with a given ID exists in the grades.csv file
# for example:
# student_id = "98A0FAE0-A19A-13D2-4BB5-CFBFD94031D1"  --> output: True
 
#2. Create a function which returns the grades of a specific student! Round to 2 decimal places.
# for example: 
#student_id = "98A0FAE0-A19A-13D2-4BB5-CFBFD94031D1"  --> output: 86.79 86.29 69.77 55.10 49.59 44.63
 
#3. Create a function which returns the best grade of the first assignment!
 
#4. Write a function which returns a dictionary containing keys as years, values as number of assignment1 in that year!
def numyyears():
    d = {}
    with open('grades.csv') as f:
        next(f)
        for l in f:
            ldata = l.split(',')
            year = ldata[2][:4]
            if year in d:
                d[year] = d[year] + 1
            else:
                d[year] = 1
    return(d)
print(numyyears())
#5. Write a function which gives the average grade of a specific assignment
 
#Exercises using algorithm description tools