
def check(string):
    numbers = ''.join([i for i in string if i.isdigit()])
    key = int(numbers)%26

    text = ""
    for i in string :
        if i.isalpha() :
            text += chr( 97 + (ord(i)+key-97) %26 )
        elif i == "-" :
            text += " "
    return [text , numbers]


file = open("input.txt" , "r")
li = file.readlines()

li = [[i[:-8] , i[-7:-2]] for i in li]


for i in li :
    temp = check(i[0])
    
    if "north" in temp[0]:
        print "Found '" + temp[0] + "' ,Code is " , temp[1]
        break
    



