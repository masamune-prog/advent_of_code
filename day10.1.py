file_obj = open("day10.txt", "r")
matrix = []
line = [x.rstrip('\n') for x in file_obj]
for i in line:
    matrix.append([x for x in i])
#print(matrix)

def isValid(s):
    ans = 0
    maping = {
        ')':'(',
        '}':'{',
        ']':"[",
        '>':'<'
    }
    points = {

        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137

    }
    stack = []
    for i in s:
        if i in maping:
            if stack and maping[i] == stack[-1]:
                stack.pop()
            else:
                ans += points[i]
                print(i)
                break
        else:
            stack.append(i)
    return ans

score = 0
for i in matrix:
        score += isValid(i)
print(score)
#print(isValid('[{[{({}]{}}([{[{{{}}([]'))
