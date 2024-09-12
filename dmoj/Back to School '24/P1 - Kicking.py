import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
graph2 = [['.' for _ in range(m)] for _ in range(n)]

for i in range(n):
    row = input().strip()
    for j in range(m):
        if row[j] != '.':
            graph[i].append((j, row[j]))
            graph2[i][j] = 'Y'

for r in range(n):
    teamA = []
    teamB = []

    for player in graph[r]:
        if player[1] == 'A':
            teamA.append(player[0])
        else:
            teamB.append(player[0])

    teamA.sort()
    teamB.sort()

    i, j = 0, 0

    # Two-pointer technique to find the closest blockers for team A
    while i < len(teamA) and j < len(teamB):
        if teamB[j] > teamA[i] and teamB[j] <= teamA[i] + k:
            graph2[r][teamA[i]] = 'N'
            i += 1  # Move to the next A
        elif teamB[j] <= teamA[i]:
            j += 1  # Move to the next B
        else:
            i += 1  # Move to the next A

    i, j = 0, 0

    # Two-pointer technique to find the closest blockers for team B
    while i < len(teamA) and j < len(teamB):
        if teamA[i] >= teamB[j] - k and teamA[i] < teamB[j]:
            graph2[r][teamB[j]] = 'N'
            j += 1  # Move to the next B
        elif teamA[i] < teamB[j]:
            i += 1  # Move to the next A
        else:
            j += 1  # Move to the next B

for row in graph2:
    print(''.join(row))
