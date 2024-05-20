Three_PointA = int(input())
Two_PointA = int(input())
One_PointA = int(input())

Three_PointB = int(input())
Two_PointB = int(input())
One_PointB = int(input())

finalA = Three_PointA * 3 + Two_PointA * 2 + One_PointA * 1
finalB = Three_PointB * 3 + Two_PointB * 2 + One_PointB * 1

if finalA > finalB:
    print('A')
elif finalB > finalA:
    print('B')
else:
    print('T')
