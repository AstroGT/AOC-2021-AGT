from copy import deepcopy

path = "day14.txt"


def parse_data(): 
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return(lines)

def split_data(data):
    init = data[0]
    ins = data[2:]
    ins = [ins[x].split(" -> ") for x in range(len(ins))]
    trnsfrm = {}
    for x in range(len(ins)):
        key = ins[x][0]
        trns1 = ins[x][0][0] + ins[x][1]
        trns2 = ins[x][1] + ins[x][0][1]
        #print(key,trns1,trns2)
        #create a transform dictionary that splits each possible chain into the appropriate couple with inserts
        trnsfrm[key] = [trns1,trns2]
    #[print(key,':',value) for key, value in trnsfrm.items()]
    return init,trnsfrm
    #print(ins)

def initPoly(init):
    polymer = {}
    for x in range(len(init)-1):
        polymer[init[x]+init[x+1]] = 1
    return polymer

init,trnsfrm = split_data(parse_data())
[print(key,':',value) for key, value in trnsfrm.items()]
poly = initPoly(init)
#print(poly)
it = 40
#Iterate through dict splitting polymer into two different ones according to key
for i in range(it):
    print(i,"/",it)
    print("--Timer--")
    poly1 = deepcopy(poly)
    print("--Timer--")
    for key in poly:
        #print("key-----",key,poly1[key])
        if poly1[key] != 0:
            poly1[key] -= poly[key]
            #print("\t",key,poly1[key])
            for x in trnsfrm[key]:
                if x in poly1:
                    poly1[x] += poly[key]
                        #print("p0",x,poly1[x])
                else:
                    poly1[x] = poly[key]
                        #print("p1",x,poly1[x])
    print("--Timer--")
    poly = deepcopy(poly1)
    print("--Timer--")
    #print(poly)

#print(poly)


#create dictionary with sum of each element
sumdict = {}
for key in poly:
    key1 = key[0]
    key2 = key[1]
    #print(key1,key2)
    #if key1 in sumdict:
        #sumdict[key1] += poly[key]
    #else:
        #sumdict[key1] = poly[key]
    if key2 in sumdict:
        sumdict[key2] += poly[key]
    else:
        sumdict[key2] = poly[key]
sumdict["N"] += 1

print(sumdict)
print(sum(sumdict.values()))
print(max(sumdict.values())-min(sumdict.values()))