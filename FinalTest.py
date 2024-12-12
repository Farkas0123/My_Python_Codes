def intersection(l1, l2):
    result = []
    for i in l1:
        if i in l2 and i not in result:
            result.append(i)
    return result

inter = intersection([1,2,3,4],[3,4,5,6])
print(inter)

def maximum(tup):
    max = tup[0]
    for i in range(1, len(tup)):
        if tup[i] > max:
            max = tup[i]
    return max

tpl = (1,2,3,4,5,6,7,8,9)
print(maximum(tpl))

def duprem(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result

print(duprem([1,1,1,1,2,3,4,5,5]))

def reverse(l):
    result = []
    for i in range(len(l), 0, -1):
        result.append(i)
    return result

print(reverse([1,2,3,4]))

#part 2------------------
def HighestSubmissionRate(input):
    dic = {}
    with open(input) as f:
        l = f.readline()
        l = f.readline()
        while l:
            akt = l.split(',')
            for i in range(2, 13, 2):
                aktmonth = akt[i].split(' ')[0].split('-')[1]
                if aktmonth in dic.keys():
                    dic[aktmonth] += 1
                else:
                    dic[aktmonth] = 1
            l = f.readline()
    maxi, month = 0,1
    for i in dic.keys():
        if maxi < dic[i]:
            maxi = dic[i]
            month = i
    months = ['January', 'February', 'March', 'April', 'May' ,'June', 'July', 'August', 'September', 'October', 'November','December']
    return months[int(month)-1]
    
print(HighestSubmissionRate('grades.csv'))

def OnTime(id):
    deadline = input('Please enter the date of the deadline (DD/MM/YYYY)')
    day = deadline.split('/')[0]
    month = deadline.split('/')[1]
    year = deadline.split('/')[2]
    with open('grades.csv') as f:
        l = f.readline()
        l = f.readline()
        yn = []
        result = True
        while l:
            akt = l.split(',')
            if akt[0] == id:
                for i in range(2, 13, 2):
                    aktsub = akt[i].split(' ')[0].split('-')
                    if aktsub[0] > year:
                        result = False
                    elif aktsub[0] == year:
                        if aktsub[1] > month:
                            result = False
                        elif aktsub[1] == month:
                            if aktsub[2] < day:
                                result = True
                            elif aktsub[2] == day:
                                result = True
                            else:
                                result = False
                        else:
                            result = True
                    else:
                        result = True
                    yn.append(result)
            l = f.readline()
        return len(list(filter(lambda x : x == False, yn))) == 0
    
print(OnTime('B73F2C11-70F0-E37D-8B10-1D20AFED50B1'))