# Assignment/exercise 1 (30 minutes)
# Write a program that displays the content of the source file ‘a.txt’!
# • First read the file character by character
# • Secondly, read the file line by line
# • Thirdly, read the whole file at once

print('>>>> BY CHAR<<<<')
f = open('a.txt', 'r', encoding = 'utf-8') #r=read, w=write, a=append
c = f.read(1)
while c:
    print(c, end='')
    c = f.read(1)
f.close()

print('>>>>BY LINE<<<<')
f = open('a.txt', 'r', encoding = 'utf-8') #r=read, w=write, a=append
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()

print('>>>>AT ONCE<<<<')
f = open('a.txt', 'r', encoding = 'utf-8') #r=read, w=write, a=append
data = f.readlines()
print(data)
f.close()

# Assignment/exercise 2 (20 minutes)
# Write a program which produces statistics on the content of the source file ‘b.txt’ as 
# follows:
# • Number of lines (use the Counting algorithm instead of len function)
# • Number of words in the file (solve it with and without split and len
# functions)
# • Number of each vowel

print('>>>>COUNT OF LINES<<<<')
with open('b.txt', encoding='utf-8') as f:
    count_of_lines = 0
    for line in f:
        count_of_lines += 1
    print(count_of_lines)

print('>>>>COUNT OF WORDS<<<<')
with open('b.txt', encoding='utf-8') as f:
    words_count = 0
    for i in f: 
        words_count += len(i.split(' '))
    print(words_count)

print('>>>>NUMBER OF VOWELS<<<<')
vowels = ['a','e','i','o','u']
with open('b.txt', encoding='utf-8') as f:
    c = f.read(1)
    countv = 0
    while c:
        if c.lower() in vowels:
            countv += 1
        c = f.read(1)
    print(countv)
    

# Assignment/exercise 3 (30 minutes)
# The source file ‘c.csv’ has a structure (BookID, BookTitle, BookAuthor, BookPrice), the 
# separator char is semicolon. Write a function which returns the lines sorted by
# BookAuthor!
# • You can use any sorting algorithm you have learned
# • Do not use built-in sorted function
# • Using this function, write the result to the ‘sorted_c.txt’ file
# • Do not use external modul




# Assignment/exercise 4 (40 minutes)
# The source file ‘c.csv’ has structure (BookID, BookTitle, BookAuthor, BookPrice). Write
# procedures to solve the following tasks:
# • List the books whose author’s name begins with the letter B
# • Display on the screen how many books each author has
# • What is the difference between the price of the most expensive and the 
# cheapest book? (Use the minimum/maximum selection algorithm)




# Assignment/exercise 5 (20 minutes)
# Write procedures/functions to implement the following file operations on the text file 
# received as a parameter:
# • create, rename, delete, append
# • use exception handling in each case
# • save them into a new module




# Homework:
# The source file ‘c.csv’ has a structure (BookID, BookTitle, BookAuthor, BookPrice). Write a 
# function which returns the average price of the books for the author received as a 
# parameter!
dic = {}
dic2 = {}

def filt(dici):
    return dict(filter(lambda item: item[1][0] > 1, dici.items()))

def avg(dici):
    for i in dic:
        if dici[i][1] in dic2.keys():
            dic2[dici[i][1]][0] += int(1)
            dic2[dici[i][1]][1] += float(dici[i][2])
        else:
            dic2[dici[i][1]] = [int(1), float(dici[i][2])]
    for i in dic2:
        dic2[i] = [int(dic2[i][0]), float(dic2[i][1]/dic2[i][0])]

with open('c.csv', encoding='utf') as f:
    line = f.readline()
    line = f.readline()
    while line:
        act = line.split(';')
        dic[act[0]] = [act[1], act[2], act[3].strip('\n')]
        line = f.readline()


print(f'Average prices')
avg(dic)
dic2 = filt(dic2)
for i in dic2:
    print(f'{i} : {dic2[i]}')