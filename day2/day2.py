import pandas as pd 

df = pd.read_csv("day2.txt",delimiter=" ")
#print (df)

input = df.values.tolist()

hor = 0
ver = 0
aim = 0

for i in range(len(input)):
    if input[i][0] == 'forward':
        hor = hor + input[i][1]
        ver = ver + aim*input[i][1]
    elif input[i][0] == 'up':
        aim = aim - input[i][1]
    elif input[i][0] == 'down':
        aim = aim + input[i][1]


print(hor)
print(ver)
prod = hor * ver
print(prod)