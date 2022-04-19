file = open('AdventCode/3./input.txt', 'r')
cont = file.read()
cont = cont.splitlines()



key = [0,0,0,0,0,0,0,0,0,0,0,0]
check = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

for x in range(0, len(cont)):
    for i in range(0, len(cont[x])):
        if cont[x][i] == "1":
            key[i] = key[i] + 1
        else:
            check[i] = check[i] + 1

print("Oxygen", key)
print("Co2", check)

for i in range(0, len(key)):
    if(key[i] > 500):
        gamma[i] = 1
    else:
        gamma[i] = 0


for i in range(0, len(key)):
    if(key[i] < 500):
        epsilon[i] = 1
    else:
        epsilon[i] = 0





str_gamma = [str(a) for a in gamma]
str_gamma = ''.join(str_gamma)
#print(str_gamma)
str_gamma = int(str_gamma, 2)

str_epsilon = [str(b) for b in epsilon]
str_epsilon = ''.join(str_epsilon)
#print(str_epsilon)
str_epsilon = int(str_epsilon, 2)


#oxygen generator
