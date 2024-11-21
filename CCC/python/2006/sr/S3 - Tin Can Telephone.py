import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
N = int(input())

if x2 != x1:
    m = (y2 - y1) / (x2 - x1)
    b1 = y1 - m * x1
else:
    m = float('inf')
    b1 = float('inf')

def intersect(x1, y1, x2, y2, x3, y3, x4, y4, m1, b1):
    if min(x1, x2) > max(x3, x4) or min(x3, x4) > max(x1, x2):
        return False

    if x3 != x4:
        m2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - m2 * x3
    else:
        m2 = float('inf')
        b2 = float('inf')

    if m1 == m2 or (m1 == float('inf') and m2 == 0) or (m2 == float('inf') and m1 == 0):
        if m1 == 0 and m2 == float('inf'):
            if x3 >= min(x1, x2) and x3 <= max(x1, x2) and y1 >= min(y3, y4) and y1 <= max(y3, y4):
                return True
        elif m2 == 0 and m1 == float('inf'):
            if x1 >= min(x3, x4) and x1 <= max(x3, x4) and y3 >= min(y1, y2) and y3 <= max(y1, y2):
                return True
        elif m1 == 0 and m2 == 0 and y1 == y3:
            if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4):
                return True
        elif m1 == float('inf') and m2 == float('inf') and x1 == x3:
            if min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
                return True
        else:
            if b1 == b2:
                return True
        return False

    if m1 == float('inf'):
        intersection_x = x1
        intersection_y = m2 * intersection_x + b2
    elif m2 == float('inf'):
        intersection_x = x3
        intersection_y = m1 * intersection_x + b1
    else:
        intersection_x = ((x2 * y1 - x1 * y2) * (x4 - x3) - (x4 * y3 - x3 * y4) * (x2 - x1)) / ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
        intersection_y = m1 * intersection_x + b1

    if min(x1, x2) <= intersection_x <= max(x1, x2) and min(y1, y2) <= intersection_y <= max(y1, y2) and min(x3, x4) <= intersection_x <= max(x3, x4) and min(y3, y4) <= intersection_y <= max(y3, y4):
        return True
    return False

count = 0

for _ in range(N):
    building_data = list(map(int, input().split()))
    corners = building_data[1:]

    blocked = False
    for i in range(0, len(corners) - 2, 2):
        if intersect(x1, y1, x2, y2, corners[i], corners[i + 1], corners[i + 2], corners[i + 3], m, b1):
            blocked = True
            break

    if blocked:
        count += 1

print(count)
