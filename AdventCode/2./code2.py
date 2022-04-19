file = open('AdventCode/2./input.txt', 'r')
cont = file.read()
cont = cont.splitlines()

horizontal = 0
depth = 0
aim = 0

def forward(x):
    global horizontal
    global depth
    global aim
    horizontal = horizontal + x
    depth = depth + (aim * x)

def up(x):
    global aim
    aim = aim - x

def down(x):
    global aim
    aim = aim + x

for i in range(0, len(cont)):
    value = cont[i][-1]
    value = int(value)
    if cont[i][0] == 'f':
        forward(value)
    elif cont[i][0] == 'd':
        down(value)
    elif cont[i][0] == 'u':
        up(value)

final = horizontal * depth
print(final)
