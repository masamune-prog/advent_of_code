file_obj = open("day8.txt", "r")
instance = 0
list = []
for x in file_obj:
    list.append(x[x.find('|') + 2:].split())

for i in list:
    for j in i:
        if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
            instance += 1
print(instance)
