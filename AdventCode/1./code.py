import math

file = open('AdventCode/1./input.txt', 'r')
cont = file.read()
cont = cont.splitlines()

for i in range(0, len(cont)):
    cont[i] = int(cont[i])


def check(cont):
    i = 0
    ans = 0
    wrong = 0

    while i+1 < len(cont):
        if(cont[i]<cont[i+1]):
            ans += 1
            i += 1
        else:
            wrong += 1
            i += 1
    print(ans, wrong)



check(cont)




def check2(cont):
    i = 0
    ans = 0
    wrong = 0

    while i < len(cont)-3:
        if(cont[i]+cont[i+1]+cont[i+2]<cont[i+1]+cont[i+2]+cont[i+3]):
            ans += 1
            i += 1
        else:
            wrong += 1
            i += 1
    print(ans, wrong)

check2(cont)
