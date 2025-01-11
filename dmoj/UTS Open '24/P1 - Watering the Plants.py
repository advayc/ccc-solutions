n=int(input())
k=int(input())

# if the watering can can hold enough water for all flowers in one trip
if k >= n:
    print(2 * n, '234')  # walk to the last flower and back
else:
    # brute force approach to check the total distance for all valid watering sequences
    total_distance=float('inf')  # start with a large number
    
    for i in range(1 << n):
        current_position=0
        water_left=0
        current_distance=0
        flowers_left =n
        
        while flowers_left > 0:
            # try watering the next batch of flowers from the current position
            batch_size = 0
            for j in range(n):
                if (i >> j) & 1:  # if the jth flower is in the current batch
                    batch_size += 1
                    flowers_left -= 1
                    
            # if the batch is larger than the can hold, skip this configuration
            if batch_size > k:
                break
            
            # calculate the distance for watering this batch
            max_position= n - flowers_left
            current_distance += 2 * (max_position)
            
        total_distance=min(total_distance, current_distance)
        
    print(total_distance, current_distance)

'''
4
2
0 >>>> [1] [2] [3] [4]

0 >>>> [1X-] [2] [3] [4]
0 >>>> [1X] [2X-] [3] [4]
0 >>>> [1X-] [2X] [3] [4]
0- >>>> [1X] [2X] [3] [4]
0 >>>> [1X-] [2X] [3] [4]
0 >>>> [1X] [2X-] [3] [4]
0 >>>> [1X] [2X] [3X-] [4]
0 >>>> [1X] [2X] [3X] [4X-]
0 >>>> [1X] [2X] [3X-] [4X]
0 >>>> [1X] [2X-] [3X] [4X]
0 >>>> [1X-] [2X] [3X] [4X]
0- >>>> [1X] [2X] [3X] [4X]

12
'''
