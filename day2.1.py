horizon = 0
depth = 0
file_obj = open("day2.txt", "r")
line = [x.rstrip('\n') for x in file_obj]
for i in line:
    inst = i.split()
    print(inst)
    if inst[0] == 'forward':
        horizon += int(inst[1])
    elif inst[0] == 'down':
        depth -= int(inst[1])
    elif inst[0] == 'up':
        depth += int(inst[1])
print(horizon)
print(depth)
print(horizon*depth)
