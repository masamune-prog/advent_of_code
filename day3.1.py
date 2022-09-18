file_obj = open("day3.txt", "r")
matrix = []
line = [x.rstrip('\n') for x in file_obj]
for i in line:
    matrix.append([x for x in i])
def common_bit(b_str):
    one = 0
    zero = 0
    for i in b_str:
        if i == '1':
            one += 1
        else:
            zero += 1
    if one>zero:
        return '1'
    else:
        return '0'

l = len(matrix[0])
b = len(matrix)

string = ''
gamma = ''
for i in range(0,l):
    for j in range(0,b):
        string += matrix[j][i]
    gamma += common_bit(string)
    string = ''
print(int(gamma, 2))
epsilon = ''
for i in gamma:
    if i == '1':
        epsilon += '0'
    else:
        epsilon += '1'
print(int(epsilon, 2))
print(int(gamma, 2) * int(epsilon, 2))
        

    