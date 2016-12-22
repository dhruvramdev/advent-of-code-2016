import numpy , sys
screen = [[0 for i in range(50)] for j in range(6)]

def pscreen():
    count = 0
    for i in screen :
        for j in i :
            if j == 0 :
                sys.stdout.write(" ")
            else :
                sys.stdout.write('o')
        sys.stdout.write("\n")
    


def extract(line):
    line = line.split(" ")
    if 'rect' in line :
        width , height = map(int , line[1].split("x"))
        for i in range(height) :
            for j in range(width) :
                screen[i][j] = 1
        
    elif 'rotate' in line :
        #pscreen()
        choice = line[1]
        number = int(line[2][2:])
        by = int(line[4])
        if choice == "row" :
            temp = numpy.array(screen[number])
            temp = numpy.roll(temp ,by)
            screen[number] = temp.tolist()
        elif choice == "column":
            li = []
            for i in screen :
                li.append(i[number])
            temp = numpy.array(li)
            temp = numpy.roll(temp ,by)
            li = temp.tolist()
            for i in range(6) :
                screen[i][number] = li[i]
        #pscreen()

        
file = open("input.txt" , "r")
data = file.read()
data = data.split('\n')
file.close()


for line in data :
    temp = extract(line)


pscreen()
