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


x1,y1,x2,y2 = parse_data()
print(x1,y1,x2,y2)
