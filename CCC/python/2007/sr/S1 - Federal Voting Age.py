n = int(input())

for i in range(n):
  year, month, day = map(int, input().split())

  if year < 1989:
    print("Yes")
  elif year == 1989 and month < 2:
    print("Yes")
  elif year == 1989 and month <= 2 and day <= 27:
    print("Yes")
  else:
    print("No")
