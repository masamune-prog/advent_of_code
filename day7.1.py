file_obj = open("day7.txt", "r")
lines = file_obj.readlines()
first_line = lines[0]
num = list(map(int, filter(None, first_line.split(','))))
mini = min(num)
maxi = max(num)
print(mini,maxi)
def crab_fuel(r):
    ans = 0
    for i in range(r+1):
        ans += i
    return ans
        
fuel = float('inf')
for i in range(mini,maxi+1):
    candi = 0
    for j in num:
        candi += crab_fuel(abs(i-j))
    fuel = min(candi,fuel)
    print(i)
print(fuel)


    
