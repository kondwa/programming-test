file="numbers.txt"

with open(file,"r") as f:
    lines = list(f)
sum = 0
for line in lines:
    sum += int(line)

print(sum)