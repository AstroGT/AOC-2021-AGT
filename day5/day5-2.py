from copy import deepcopy

path ="day5.txt"

def parse_data(): 
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    strarr = []
    for x in range(len(lines)):
        strarr.append(lines[x].split("->"))
    xy1 = [row[0] for row in strarr]
    xy1 = [x.strip() for x in xy1]
    xy2 = [row[1] for row in strarr]
    xy2 = [x.strip() for x in xy2]
    xy1 = [x.split(",") for x in xy1]
    xy2 = [x.split(",") for x in xy2]
    x1 = [row[0] for row in xy1]
    y1 = [row[1] for row in xy1]
    x2 = [row[0] for row in xy2]
    y2 = [row[1] for row in xy2]
    #print(x1,"\n",y1,"\n",x2,"\n",y2,"\n")
    return x1,y1,x2,y2

def findsign(num2,num1):
    if num2 - num1 > 0:
        return 1
    elif num2 - num1 < 0:
        return -1
    else:
        return 0

def createVentMap(xc1,xc2,yc1,yc2):
    ventmap = {}
    #create vent map with size maxX,maxY
    maxX = max(max(xc1),max(xc2))
    maxY = max(max(yc1),max(yc2))
    for i in range(maxX+1):
        for j in range(maxY+1):
            ventmap["{},{}".format(i,j)] = 0
    #print(ventmap.keys())
    lines = createlines(xc1,xc2,yc1,yc2)
    #print(lines)
    for j in range(len(lines)):
        for k in range(len(lines[j])):
            ventmap[lines[j][k]] += 1
    #print(ventmap)
    return ventmap

def createlines(xd1,xd2,yd1,yd2):
    lines = []
    for x in range(len(xd1)):
        line = []
        #print(xd1[x],yd1[x],xd2[x],yd2[x])
        signx = findsign(xd2[x],xd1[x])
        signy = findsign(yd2[x],yd1[x])
        if signx == 1:
            xd2[x] += 1
        if signx == -1:
            xd2[x] -= 1
        if signy == 1:
            yd2[x] += 1
        if signy == -1:
            yd2[x] -= 1
        if signx == 0:
            signx = 1
        if signy == 0:
            signy = 1
        #print(xd1[x],yd1[x],xd2[x],yd2[x])    
        if xd1[x] == xd2[x]:
            for i in range(yd1[x],yd2[x],signy):
                line.append("{},{}".format(xd1[x],i))
        elif yd1[x] == yd2[x]:
            for i in range(xd1[x],xd2[x],signx):
                line.append("{},{}".format(i,yd1[x]))
        else:
            lineX = list(range(xd1[x],xd2[x],signx))
            lineY = list(range(yd1[x],yd2[x],signy))
            #print(lineX,lineY)
            for i in range(len(lineX)):
                #print(len(lineX),len(lineY))
                line.append("{},{}".format(lineX[i],lineY[i]))
        lines.append(deepcopy(line))
    return lines

def countOverlap(ventmap):
    sum = 0
    for x in ventmap.values():
        if x >= 2:
            sum += 1
    return sum

x1,y1,x2,y2 = parse_data()
x1 = list(map(int,x1))
x2 = list(map(int,x2))
y1 = list(map(int,y1))
y2 = list(map(int,y2))
#print(x1,y1,x2,y2)
ventmap = createVentMap(x1,x2,y1,y2)
sum = countOverlap(ventmap)
print(sum)