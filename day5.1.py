file_obj = open("day5.txt", "r")
points = 0
c_dict = {}
mapping = []
def vert(c1,c2):
    if (c1[1] == c2[1]):
        return True
def not_diagonal(coord1,coord2):
    #2 arrays 
    if (coord1[0] == coord2[0]) or (coord1[1] == coord2[1]):
        return True
    else:
        return False
def dia_add(c1,c2):
    steps = abs(c1[0]-c2[0]) + 1
    #is right side of cross
    if (c1[0]-c2[0]) == (c1[1]-c2[1]):
        s_i,s_j = min(c1,c2)
        for step in range(0,steps):
            if (s_i+step,s_j+step) in c_dict:
                c_dict[(s_i+step,s_j+step)] += 1
            else:
                c_dict[(s_i+step,s_j+step)] = 1
    else:
        #settle left side of the cross
        #find if x or y is increasing or decreasing
        s_i,s_j = min(c1,c2)
        for step in range(0,steps):
            if (s_i+step,s_j-step) in c_dict:
                c_dict[(s_i+step,s_j-step)] += 1
            else:
                c_dict[(s_i+step,s_j-step)] = 1


def vert_add(c1,c2):
    #the y coord the same
    p = 0
    y = c2[1]
    bigger = max(c2[0],c1[0])
    smaller = min(c2[0],c1[0])
    for i in range(smaller,bigger+1):
        if (i,y) in c_dict:
            c_dict[(i,y)] += 1
        else:
            c_dict[(i,y)] = 1
def hori_add(c1,c2):
    #the y coord the same
    p = 0
    x = c2[0]
    bigger = max(c2[1],c1[1])
    smaller = min(c2[1],c1[1])
    for i in range(smaller,bigger+1):
        if (x,i) in c_dict:
            c_dict[(x,i)] += 1
        else:
            c_dict[(x,i)] = 1
for line in file_obj:
    dot1, dot2 = line.replace('\n', '').split(' -> ')
    c1 = tuple(map(int, dot1.split(',')))
    c2 = tuple(map(int, dot2.split(',')))
    mapping.append([c1,c2])
#print(mapping)
for i in mapping:
    c1 = i[0]
    c2 = i[1]
    if not_diagonal(c1,c2):
        #print(c1,c2)
        if vert(c1,c2):
            vert_add(c1,c2)
        else:
            hori_add(c1,c2)
    else:
        dia_add(c1,c2)

for i in sorted(c_dict):
    #print(i,c_dict[i])
    if c_dict[i] >= 2:
        points += 1
print(len(c_dict))
print(points) 

