import hashlib

code = "reyedfim"
#code = "abc"
passcode = [0,0,0,0,0,0,0,0]
count = [0,1,2,3,4,5,6,7]

i = 0

while (count != []) :
    temp = code + str(i)
    md5 = hashlib.md5(temp.encode('utf-8')).hexdigest()
    if md5[:5] == "00000" and md5[5].isdigit():
        #print md5 , i
        number = int(md5[5])
        if number in count :
            passcode[number] = md5[6]
            count.remove(number)
        
    
    i += 1

print ''.join(passcode)
