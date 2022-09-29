file_obj = open("day9.txt", "r")
lines = file_obj.readlines()
#get board
boards = []
mat = []
#extract matrix
for line in lines:
    #print(line)
    for i in line:
        if i != "\n":
            mat.append(int(i))
        else:
            boards.append(mat)
            mat = []
#print(boards)
#perform a search
def calc_risk(matrix):
    ex_risk = {}
    score = 0
    height = len(matrix)
    width = len(matrix[0])
    search = [[-1,0],[1,0],[0,1],[0,-1]]
    for i in range(height):
        for j in range(width):
            position = matrix[i][j]
            for x,y in search:
                if (i+x >= 0) and (i+x<height) and (j+y >= 0) and (j+y<width):
                    #print(i+x,j+y)
                    if matrix[i+x][j+y] <= position:
                        ex_risk[(i,j)] = 0
    risk = []
    for i in range(height):
        for j in range(width):
            if (i,j) not in ex_risk.keys():
                risk.append([i,j])
    return risk

print(calc_risk(boards))
