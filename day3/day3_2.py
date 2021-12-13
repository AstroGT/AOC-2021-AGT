from os import X_OK
from typing import NewType


file = open("day3.txt")
input = file.read().splitlines()
input = [str(i) for i in input]
file.close()
#print(input) #Debug

OGR = 0
CSR = 0

def find_digit(data,loc,type):
    mc_digit = 0
    lc_digit = 0
    sum1 = 0
    sum0 = 0
    for j in range(len(data)):
        if data[j][loc] == "1":
            sum1 = sum1 + 1
        if data[j][loc] == "0":
            sum0 = sum0 + 1
        #print("\t\t\t\t input[j][loc]",j)
    if sum1 > sum0:
        mc_digit = 1
        lc_digit = 0
    elif sum1 < sum0:
        mc_digit = 0
        lc_digit = 1
    elif sum1 == sum0:
        mc_digit = 2
        lc_digit = 2

    if type == "most":
        return mc_digit
    elif type == "least":
        return lc_digit

def calc_Val(data,select):
    for i in range(len(data[0])):
            new_data = []
            digit = find_digit(data,i,select)
            for j in range(len(data)):
                #print(" \t\t\t","digit",digit)
                #print("data[j][i]",data)
                if digit == 2:
                    #print(" \t\t","new data append data[j]",data[j])
                    if select == "most":
                        if data[j][i] == str(1):
                            new_data.append(data[j])
                            #print("data[j]",data[j])
                    else:
                        if data[j][i] == str(0):
                            new_data.append(data[j])
                elif data[j][i] == str(digit):
                    #print(" \t\t","new data append data[j]",data[j])
                    new_data.append(data[j])
                #print("\tnew_data",new_data)
            data = new_data
            print("data",data)
            if len(data) == 1:
                break
    return data
OGR = calc_Val(input,"most")
CSR = calc_Val(input,"least")
print("\n OGR = ",OGR)
print("\n CSR = ",)
print("\n Ans = ", int(OGR[0],2)*int(CSR[0],2))
            

