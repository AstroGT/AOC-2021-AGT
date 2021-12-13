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

def remove_diagonals(x1,x2,y1,y2):
    for i in range(len(x1)):
        if (x1[i] != x2[i]) & (y1[i] != y2[i]):
            x1[i] = -999
            x2[i] = -999
            y1[i] = -999
            y2[i] = -999
    x1 = [j for j in x1 if j != -999]
    x2 = [j for j in x2 if j != -999]
    y1 = [j for j in y1 if j != -999]
    y2 = [j for j in y2 if j != -999]
    return x1,y1,x2,y2

def remove_lines(x1,x2,y1,y2):
    for i in range(len(x1)):
        if (x1[i] != x2[i]) & (y1[i] != y2[i]) & (abs(int(y2[i])-int(y1[i]))-abs(int(x2[i])-int(x1[i])) != 0):
            x1[i] = -999
            x2[i] = -999
            y1[i] = -999
            y2[i] = -999
    x1 = [j for j in x1 if j != -999]
    x2 = [j for j in x2 if j != -999]
    y1 = [j for j in y1 if j != -999]
    y2 = [j for j in y2 if j != -999]
    return x1,y1,x2,y2

def create_key_list(xc1,xc2,yc1,yc2):
    #print(xc1,xc2,yc1,yc2)
    keys = []
    #make a list of x co-ords in scope
    keysX = [x for x in range(int(min(int(xc1),int(xc2))),int(max(int(xc1),int(xc2)))+1)]
    #print(keysX)
    if xc1 > xc2:
        keysX.reverse()
    #make a list of y co-ords in scope
    keysY = [y for y in range(int(min(int(yc1),int(yc2))),int(max(int(yc1),int(yc2)))+1)]
    #print(keysY)
    if yc1 > yc2:
        keysY.reverse()
    #combine x and y coords into an x-y list of keys
    if (xc1 != xc2) & (yc1 != yc2):
        keys = []
        for i in range(len(keysX)):
            currKey = "{},{}".format(keysX[i],keysY[i])
            #print(currKey)
            keys.append(currKey)
    else:
        keys = [["{},{}".format(i,j) for i in keysX] for j in keysY]
    #print(keys)
    return keys

def find_covered_points(x1,x2,y1,y2):
    # find max x and y co-ords
    maxX = int(max([max(list(map(int,x1))),max(list(map(int,x2)))]))
    maxY = int(max([max(list(map(int,y1))),max(list(map(int,y2)))]))
    print(maxX,maxY)
    # create a grid dict with all possible keys
    grid = {}
    for x in range(maxX+1):
        for y in range(maxY+1):
            grid["{},{}".format(x,y)] = 0
    #print(grid)
    for i in range(len(x1)):
        # create a list of keys that is formed from each line
        Keys = create_key_list(x1[i],x2[i],y1[i],y2[i])
        print(Keys)
        # sum up each matched key from list
        #print (range(len(Keys[0])))
        if len(Keys[0]) == 1:
            for j in range(len(Keys)):
                grid[Keys[j][0]] = grid[Keys[j][0]] + 1
                #print(Keys[j][0])
        elif len(Keys) == 1:
            for j in range(len(Keys[0])):
                grid[Keys[0][j]] = grid[Keys[0][j]] + 1
                #print(Keys[0][j])
        else:
            for i in range(len(Keys)):
                    #print(Keys[i])
                    grid[Keys[i]] = grid[Keys[i]] + 1
    return grid

def greaterthaneq(val,cond):
    if val >= cond:
        return 1
    else:
        return 0

x1,y1,x2,y2 = parse_data()
# x1,y1,x2,y2 = remove_lines(x1,x2,y1,y2)
grid = find_covered_points(x1,x2,y1,y2)
gridSum = sum(1 for x in grid.values() if greaterthaneq(x,2))
#print(grid)
print(gridSum)
# print(x1,"\n",y1,"\n",x2,"\n",y2,"\n")