file_obj = open("day11.txt", "r")
matrix = []
line = [x.rstrip('\n') for x in file_obj]
for i in line:
    matrix.append([int(x) for x in i])
#print(matrix)
#def count_flash(matrix)
flashes = 0
row = len(matrix)
col = len(matrix[0])
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (-1,1), (-1,-1), (1,-1)]
for i in range(row):
    for j in range(col):
        position = matrix[i][j]
        matrix[i][j] += 1
        for x,y in directions:
            # check that surroundings not more than 9 add the surroundings and set itself to 0
            if (i+x >= 0) and (i+x<row) and (j+y >= 0) and (j+y<col):
                #first check if the surrounding coords is valid first
                matrix[i+x][j+y] += 1
for i in range(row):
    for j in range(col):
        if matrix[i][j] >= 9 :
            matrix[i][j] = 0

print(matrix)
