
file = open("day1-1_i.txt")
input = file.readlines()
input = [int(i) for i in input]
file.close()
#print(input) Debug

sum = 0

for i in range(len(input)-3):
    w1 = input[i]+input[i+1]+input[i+2]
    w2 = input[i+1]+input[i+2]+input[i+3]
    if (w2>w1):
        sum = sum + 1

print(sum)
