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

def check(string):
    for i in range(len(string) - 3):
        #print string[i:i+2] , string[i+2:i+4][::-1] 
        if string[i:i+2] == string[i+2:i+4][::-1] and string[i] != string[i+1]:
            return True

    return False

def evaluate( li ):
    result = li[0]
    for i in li :
        result = result or i
    return result

count = 0 

for line in lines :
    line = line.strip("\n")
    outer , inner = extract(line)
    outer = [check(i) for i in outer]
    inner = [check(i) for i in inner]
    
    #print outer , evaluate(outer) , inner , evaluate(inner)

    if not (evaluate(inner)) and (evaluate(outer)) :
        count += 1


print count

    
    

