file = open('input.txt' , 'r')
data = file.read()
file.close()

#data = "A(2x2)BCD(2x2)EFG"

l = len(data)
print "Length of Input Uncompressed String -" , l

decompressed = ""
i = 0

while (i<l) :
    if data[i] == '(' :
        j = i+3
        while data[j] != ')'  :
            j =j+1
        number , repeat = map( int , data[i+1:j].split("x"))
        string = data[j+1:j+number+1]
        for i in range(repeat):
            decompressed += string
        i = j + number + 1  
    elif data[i] in ['\n' ,  ' ' , '\t']:
        i=i+1

    else :
        decompressed += data[i]
        i = i + 1

print len(decompressed) 

