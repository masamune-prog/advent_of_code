line = ""
with open('day6.txt') as f:
    line = f.readline()
nums = line.split(",")

#print (nums)

fishes = [0,0,0,0,0,0,0,0,0]

for fish in nums:
  fishes[int(fish)] = fishes[int(fish)]+1

print (f"Start:{fishes}")

def newday(day):
  newfishborn = False
  newfishCount = 0
  if (fishes[0]>0):
    newfishborn = True
    newfishCount = fishes[0]
  fishes.append(fishes.pop(0))
  if newfishborn == True:
    fishes[6] = fishes[6] + newfishCount
  print (f"day {x+1}:{fishes}")

for x in range(256):
  newday(x)


total = 0
for fish in fishes:
  total = total + fish
print()
print(f"Total Fish Population is:{total}")
