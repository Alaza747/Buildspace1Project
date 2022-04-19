file = open('AdventCode/2./input.txt', 'r')
cont = file.read()
cont = cont.splitlines()

horizontal = 0
depth = 0

def forward(x):
    global horizontal
    horizontal = horizontal + x

def up(x):
    global depth
    depth = depth - x

def down(x):
    global depth
    depth = depth + x

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
