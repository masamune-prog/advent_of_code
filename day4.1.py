#get the winning numbers
import copy
file_obj = open("day4.txt", "r")
lines = file_obj.readlines()
first_line = lines[0]
num = list(map(int, filter(None, first_line.split(','))))
#get board
boards = []
mat = []
#extract matrix
for line in lines[2:]:
    #print(line)
    if line == "\n":
        boards.append(mat)
        mat = []
    else:
        mat.append(list(map(int, filter(None, line.split(' ')))))
boards.append(mat)
clean = copy.deepcopy(boards)
# starts from line index 2
#bingo takes matrix and finds the index of number that solves it
def bingo(matrix,w_nums):
    #win conditions, any of the padding becomes 5
    #pad the 5x5 matrix
    #add horizontal 0
    matrix.append([0,0,0,0,0])
    #add vertical
    for i in matrix:
        i.append(0)
    #print(matrix)
    #cycle through the winning num
    for num in range(len(w_nums)):
        for i in range(0,5):
            for j in range(0,5):
                if w_nums[num] == matrix[i][j]:
                    matrix[i][5] += 1
                    matrix[5][j] += 1
                    if matrix[i][5] == 5 or matrix[5][j] == 5:
                        return num

#find fastest winning board
#print(boards)
fastest_board = -1
winning_index = -1


for board in range(len(boards)):
    candidate = bingo(boards[board],num)
    if winning_index < candidate:
        winning_index = candidate
        fastest_board = board
#find ans
print(fastest_board)
print(winning_index)
#print(num)
points = 0
#find total sum - the latest winning num
for i in clean[fastest_board]:
    for j in i:
        if j not in num[0:winning_index+1]:
            points += j
print(num[0:winning_index+1])   
print(points)
points *= num[winning_index]
print(points)

