file = open("day4.txt")
input = file.read().splitlines()
input = [str(i) for i in input]
file.close()

def splitinput(data):
    squares = []
    numbers = data[0]
    numbers = numbers.split(",")
        
    data.pop(0)
    row = 0
    col = 0
    for i in range(data.count('')):
        squares.append([])
        for j in range(5):
            squares[i].append([])
            if data[row] == '':
                row += 1
            for k in range(5):
                currVal = int(data[row][col:(col+2)])
                col += 3
                squares[i][j].append(currVal)
            col = 0
            row += 1
            if row == len(data):
                return squares,numbers

def createBoolmatrix(data):
    booleanMatrix = []
    for i in range(data.count('')):
        booleanMatrix.append([])
        for j in range(5):
            booleanMatrix[i].append([])
            for k in range(5):
                booleanMatrix[i][j].append(0)
    return booleanMatrix


def markNumbers(sq,boolsq,num):
    for i in range(len(num)):
        curr_ind = 0
        for j in range(len(sq)):
            curr_ind = j
            for k in range(5):
                for l in range(5):
                    if int(sq[j][k][l]) == int(num[i]):
                        boolsq[j][k][l] = 1
        winCond,winSq = testwin(boolsq)
        if winCond == 1:
            return sq, boolsq, num[i], winSq

def testwin(boolmat):
    for j in range(len(boolmat)):
            for k in range(5):
                x = []
                if(all(boolmat[j][k]) == 1):
                    print("ROW MATCH!")
                    return 1,j
                for l in range(5):
                    x.append(boolmat[j][l][k])
                if(all(x) == 1):
                    print("COL MATCH!")
                    return 1,j
    return 0,0

def calcScore(sq,bm,winSq,winNo):
    unmrkSum = 0
    for k in range(5):
        for l in range(5):
            if(bm[winSq][k][l] == 0):
                unmrkSum += int(sq[winSq][k][l])
    score = int(unmrkSum) * int(winNo)
    return score

sq,nu = splitinput(input)
bm = createBoolmatrix(input)

sq,bm,winNo,winSq = markNumbers(sq,bm,nu)


print("Calld Numbrs: ",nu)
print("Input Matrix: ", len(sq),len(sq[0]),len(sq[0][0]))
print("Check Matrix: ", len(bm),len(bm[0]),len(bm[0][0]))
print("Winin Number: ", winNo)
print("Winin Square: ", winSq)
print("\nSCORE! -",calcScore(sq,bm,winSq,winNo))


