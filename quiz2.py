def filter_list (l):
    result = []
    for i in range(len(l)):
        if l[i] >= 0:
            result.append(l[i])
    return result

def sum(l):
    result = 0
    for i in range(len(l)):
        result += l[i]
    return result

def avg(d):
    result = []
    for i in d:
        if sum(i[1])/len(i[1]) > 80:
            result.append(i[0])
    for i in range(len(result)):
        if i < len(result)-1:
            print(result[i], end=", ")
        else:
            print(result[i])

def findupper(t):
    result = 0 
    with open(t, encoding='utf - 8' ) as f:
        c = f.read(1)
        while c:
            if c != c.lower():
                result += 1
            c = f.read(1)
    print(result)
    
#print(filter_list([4, 5, -2, 0, 3, -8]))
# students = [ ('Alice', [85, 92, 85]), ('Bob', [78, 75, 82]), ('Charlie', [92, 85, 78]) ]           
# avg(students)
findupper('a.txt')