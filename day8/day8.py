from os import cpu_count

path = "day8.txt"

def parse_data(): 
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return(lines)

input = parse_data()
keys = [x.split(" | ")[0] for x in input]
data = [x.split(" | ")[1] for x in input]
keys = [x.split(" ") for x in keys]
data = [x.split(" ") for x in data]

#print(keys,data)
sumdigits = 0

for i in range(len(data)):
    cData = data[i]
    match = {}
    #find matching keys:
    for j in range(len(cData)):
        print(i,len(cData[j]))
        if (len(cData[j]) == 3 or len(cData[j]) == 4 or len(cData[j]) == 2 or len(cData[j]) == 7):
            print("match")
            sumdigits += 1

print(sumdigits)