path = "day6.txt"

def parse_data(): 
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return(lines)

def update_fish(fish,iterations):
    #convert fish to array
    fish = fish.split(",")
    fish = list(map(int,fish))
    #init list fishBucket[timer] = totalfishwithtimer 
    fishbucket = [0]*9
    #init fishbucket with input
    for i in range(len(fish)):
        fishbucket[fish[i]] += 1
    #iterate over fishbucket
    for x in range(iterations):
        print("iter: ",x+1)
        spawn = fishbucket[0]
        for j in range(0,len(fishbucket)-1):
            fishbucket[j] = fishbucket[j+1]
        fishbucket[6] = fishbucket[6]+spawn
        fishbucket[8] = spawn
        print(fishbucket)
    return(sum(fishbucket))

input = parse_data()[0]
#print(input)
#input = input.replace(",","")
iterations = 256
out = update_fish(input,iterations)

#print(input)    
print(out)