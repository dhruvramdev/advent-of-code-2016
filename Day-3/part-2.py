import re

file = open("input.txt" , "r")

triangles = file.readlines()

triangles = [map(int , re.split('\\s+' , i.strip())) for i in triangles]

count = 0

l = len(triangles)

for i in range(0,l,3) :
    for j in range(3) :
        temp_list = [ triangles[i][j] , triangles[i+1][j] , triangles[i+2][j]]
        #print temp_list
        temp_list.sort()
        if temp_list[2] < temp_list[0] + temp_list[1] :
            count += 1
    

print count 
