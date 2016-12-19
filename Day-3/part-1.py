import re

file = open("input.txt" , "r")

triangles = file.readlines()

triangles = [map(int , re.split('\\s+' , i.strip())) for i in triangles]

count = 0

for i in triangles :
    i.sort()
    if i[2] < i[0] + i[1] :
        count += 1


print count , len(triangles)
