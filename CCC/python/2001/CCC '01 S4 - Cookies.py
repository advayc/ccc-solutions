import math
n=int(input())
chips=[list(map(int, input().split())) for _ in range(n)]
#chip[0] == x
min_x = min(chip[0] for chip in chips)
max_x = max(chip[0] for chip in chips) 
#chip[1] == y
min_y = min(chip[1] for chip in chips)
max_y = max(chip[1] for chip in chips)

# The diameter is the diagonal of the rectangle
diameter = math.sqrt((max_x - min_x)**2 + (max_y - min_y)**2)

print(round(diameter, 2))

