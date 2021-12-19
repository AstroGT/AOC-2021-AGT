from os import cpu_count


path = "day7.txt"

def parse_data(): 
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return(lines)

def findBestPos(data):
    BP = 999999999
    BPF = 999999999
    #find maximum and minimum position of crabs
    cPosMin = min(data)
    cPosMax = max(data)
    #iterate through lines with minimum and max position
    for i in range(cPosMin,cPosMax,1):
        #calculate sum of distance (fuel) to each point
        BPF_itr = 0
        for j in range(len(data)):
            expsum = 0
            for k in range(abs(data[j]-i)+1):
                expsum += k
            BPF_itr += expsum
        #if minimum: BP and BPF update
        if BPF_itr < BPF:
            BPF = BPF_itr
            BP = i
        print(i,"/",cPosMax-cPosMin)
    return (BP,BPF)
input = parse_data()[0]
input = input.split(",")
input = list(map(int,input))
print(findBestPos(input))