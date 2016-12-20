import hashlib

code = "reyedfim"
#code = "abc"
passcode = ""
count = 0

i = 0

while (count<8) :
    temp = code + str(i)
    md5 = hashlib.md5(temp.encode('utf-8')).hexdigest()
    if md5[:5] == "00000" and type(md5[5] == 'int' ) :
        print 1
        
    
    i += 1

print passcode
