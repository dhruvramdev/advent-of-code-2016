file = open('input.txt' , 'r')
data = file.read()
file.close()

#data = "(27x12)(20x12)(13x14)(7x10)(1x12)A"

print "Length of Input Uncompressed String -" , len(data)

def find_len(data):
    length = 0
    l = len(data)
    i = 0

    while (i<l) :
        if data[i] == '(' :
            j = i+3
            while data[j] != ')'  :
                j =j+1
            number , repeat = map( int , data[i+1:j].split("x"))
            string = data[j+1:j+number+1]
            if '(' in string :
                length += find_len(string) * repeat
            else :
                length += number * repeat 
            i = j + number + 1  
        elif data[i] in ['\n' ,  ' ' , '\t']:
            i=i+1

        else :
            length += 1
            i = i + 1

    return length

print find_len(data)
