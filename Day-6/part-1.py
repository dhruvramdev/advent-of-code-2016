file = open("input.txt" , "r")
li = []
code = ""
lines = file.readlines()
for i in range(8):
    di = {}
    li.append([line[i] for line in lines])
    for j in li[i] :
        if j in di :
            di[j] += 1
        else :
            di[j] = 1
    #print di
    #print 
    code += max(di , key= di.get)    

print code
