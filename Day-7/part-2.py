file = open("input.txt")
lines = file.readlines()
file.close()

def extract(string):
    string = string.replace( "[" , ",")
    string = string.replace( "]" , ",")
    li = string.split(",")
    outer = li[::2]
    inner = li[1::2]
    return outer , inner

def check(inner , outer):
    found = []
    for string in outer :
        for i in range(len(string) - 2):
            if string[i] == string[i+2] and string[i] != string[i+1]:
                found.append(string[i:i+3])
    #print found
    if found != [] :
        for i in found :
            bab = i[1:] + i[1]
            for x in inner :
                if bab in x :
                    #print i , bab
                    return True
    return False

count = 0 

for line in lines :
    line = line.strip("\n")
    outer , inner = extract(line)
    if check(inner , outer):
        count += 1


print count

    
    

