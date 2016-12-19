from operator import itemgetter

def check(string , checksum):
    dic = {}
    numbers = ''
    
    for i in string :
        if i.isalpha() :
            if i in dic :
                dic[i] += 1
            else :
                dic[i] = 1
        elif i.isdigit() :
            numbers += i

    temp = sorted(dic.items())
    temp.sort(key=itemgetter(1) , reverse = True)

    c = ''.join([temp[i][0] for i in range(5)])

    #print temp ,c ,checksum

    if (c == checksum) :
        return int(numbers)
    return 0





file = open("input.txt" , "r")
li = file.readlines()



li = [[i[:-8] , i[-7:-2]] for i in li]
count = 0

for i in li :
    count += check(i[0] , i[1])    
    
print count


