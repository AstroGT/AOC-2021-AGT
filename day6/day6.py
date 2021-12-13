path = "day6.txt"

def parse_data(): 
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return(lines)

def fishLogic(x):
    if x != 0:
        return x-1
    else:
        return 6

def update_fish(fish):
    fish = list(fish)
    #print("fish\n",fish)
    #iterate through array
    zeroCnt = fish.count(0)
    #subtract 1 from each element
    fish = [fishLogic(x) for x in fish]
    
    #add timer8 fish according to number of zeros
    newFish = [8]*zeroCnt
    #print(newFish)
    #print(fish)
    if len(newFish) != 0:
        fish.extend(newFish)
    #print(fish)
    return(fish)
input = parse_data()
input = input[0].split(",")
input = list(map(int,input))


for x in range(256):
    print(x,"/256")
    input = update_fish(input)

#print(input)    
print(len(input))