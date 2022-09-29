file_obj = open("day9.txt", "r")
from collections import deque
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

risky = calc_risk(boards)

def findBasin(grid):
    if not grid:
            return 0
    can = []
    visited = set(())
    col = len(grid[0])
    rows = len(grid)
    def bfs(start):
        area = 1
        queue = deque([start])
        while queue:
            sx, sy = queue.popleft()
            visited.add((sx, sy))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                x = sx + dx
                y = sy + dy
                if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and (x, y) not in visited and grid[x][y] != 9:
                    visited.add((x, y))
                    queue.append((x, y))
                    area += 1
        can.append(area)



    for i in range(rows):
        for j in range(col):
            if grid[i][j] != 9 and ((i,j) not in visited):
                bfs((i,j))

    if not can:
        return 0
    else:
        return can
can = sorted(findBasin(boards))[::-1]
ans = can[0] * can[1] * can[2]
print(ans)
