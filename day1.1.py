file_obj = open("day1.txt", "r")
  
# splitting the file data into lines
lines = [x.rstrip('\n') for x in file_obj]
#print(lines)
file_obj.close()
c = 0
s = lines[0]
for i in range(1,len(lines)):
    if s<lines[i]:
        c+=1
        #print(lines[i])
    s = lines[i]
print(c)
