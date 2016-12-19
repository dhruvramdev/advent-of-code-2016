import matplotlib.pyplot as plt


li = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"
#li = "R2, R2, R2 , R2"

li = [i.strip() for i in li.split(",")]

pos = [0,0]
x = []
y = []
direction = "y"
rules = {
        
        "L" : ["x" , "y" , "-x" , "-y" ] ,
        "R" : ["x" , "-y", "-x" ,  "y" ]
    }



def find(hint):
    temp = rules[hint]

    return temp[(temp.index(direction)+1)%4]

def move(units , direction) :
    if direction == "x" :
        pos[0] += units
    elif direction == "-x" :
        pos[0] -= units
    elif direction == "y" :
        pos[1] += units
    elif direction == "-y" :
        pos[1] -= units
        
    
    
for i in li :
    direction = find(i[0])
    move( int(i[1:] ) , direction)
    #print i[0] , i[1:] , pos
    x.append(pos[0])
    y.append(pos[1])

#part 1 answer
print "Distance is" , sum([abs(i) for i in pos]) , "blocks"

#part 2 answer by graph
plt.plot(x, y)
plt.show()

#Find the first intersection point by zooming in maptolib .. :p
