file_obj = open("day10.txt", "r")
matrix = []
line = [x.rstrip('\n') for x in file_obj]
for i in line:
    matrix.append([x for x in i])

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
    corruppted = []
    for i in s:
        if i in maping:
            if stack and maping[i] == stack[-1]:
                stack.pop()
            else:
                #the line is corruppted
                return False
                break
        else:
            stack.append(i)
    return True

def fix(s):
    ans = 0
    maping = {
        ')':'(',
        '}':'{',
        ']':"[",
        '>':'<'
    }
    inv_map = {v: k for k, v in maping.items()}
    points = {

        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4

    }
    stack = []
    complete = []
    for i in s:
        if i in maping:
            if stack and maping[i] == stack[-1]:
                stack.pop()
        else:
            stack.append(i)
    for j in stack:
        complete.append(inv_map[j])
    for i in complete[::-1]:
        ans *= 5
        ans += points[i]
    return ans




score = []
for i in matrix:
        if isValid(i):
            score.append(i)
final = []
for i in score:
    final.append(fix(i))
final = sorted(final)
index = len(final) // 2
print(final[index])
