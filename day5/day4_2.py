from copy import deepcopy

file = open("test_in.txt")
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
    testind = list(range(len(sq)))
    alreadywon = []
    waboolsq = []
    outind = 0
    actWinSq = 0
    for i in range(len(num)):
        for j in range(len(sq)):
            for k in range(5):
                for l in range(5):
                    if int(sq[j][k][l]) == int(num[i]):
                        boolsq[j][k][l] = 1
        winSq = testwin(boolsq,testind)
        updatewin = 1
        if winSq != -1:
            for element in alreadywon:
                if element in testind:
                    testind.remove(element)
            for x in range(len(alreadywon)):
                if winSq == alreadywon[x]:
                    #print("Already Won")
                    updatewin = 0
            print(alreadywon)
                
            if updatewin == 1:
                alreadywon.append(winSq)
                print("Updating Win")
                #print(winSq)
                #print(boolsq)
                waboolsq = deepcopy(boolsq)
                actWinSq = winSq
                outind = i-1
    print(waboolsq)
    return sq, waboolsq, num[outind], actWinSq

def testwin(boolmat,testind):
    for j in testind:
        #print(j)
        for k in range(5):
            x = []
            if(all(boolmat[j][k]) == 1):
                print("ROW MATCH!")
                return j
            for l in range(5):
                x.append(boolmat[j][l][k])
            if(all(x) == 1):
                print("COL MATCH!")
                return j
    return -1

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

sq,wbm,winNo,winSq = markNumbers(sq,bm,nu)
#print(wbm)

print("Calld Numbrs: ",nu)
print("Input Matrix: ", len(sq),len(sq[0]),len(sq[0][0]))
print("Check Matrix: ", len(bm),len(bm[0]),len(bm[0][0]))
print("Winin Number: ", winNo)
print("Winin Square: ", winSq)
print("\nSCORE! -",calcScore(sq,wbm,winSq,winNo))


