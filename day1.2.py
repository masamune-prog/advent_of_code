start = 0
end = 2
file_obj = open("day1.1.txt", "r")
  
# splitting the file data into lines
line = [x.rstrip('\n') for x in file_obj]
lines = list(map(int, line))
#print(len(lines))
#print(lines)
file_obj.close()
val = []
c = 0
#print(lines)
while end+1 <= len(lines):
    val.append(sum(lines[start:end+1]))
    start += 1
    end += 1
c = 0
s = val[0]
for i in range(1,len(val)):
    if s<val[i]:
        c+=1
        #print(lines[i])
    s = val[i]
print(c)

