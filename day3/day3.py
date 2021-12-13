file = open("dt.txt")
input = file.read().splitlines()
input = [str(i) for i in input]
file.close()
#print(input) #Debug

gamma = "A"
epsilon = "A"


for i in range(len(input[0])):
    sum1 = 0
    sum0 = 0
    for j in range(len(input)):
        if input[j][i] == "1":
            sum1 = sum1 + 1
        else:
            sum0 = sum0 + 1
    if sum1 > sum0:
        gamma += str(1)
        epsilon += str(0)
    else:
        gamma += str(0)
        epsilon += str(1)

gamma = gamma[1:]
epsilon = epsilon[1:]

gamma = int(gamma,2)
epsilon = int(epsilon,2)

print(gamma)
print(epsilon)
print(gamma*epsilon)





