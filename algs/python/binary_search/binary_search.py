# return the index of a target number from sorted array

def binary_search(array: list, target):
    low = 0 # get first index
    high = len(array) - 1 # get last index

    while high > low:
        middle = (high + low) // 2 
        if target > array[middle]:
            low = middle + 1
        else:
            high = middle

    return low


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)) # returns the index 1

'''
ar = list(map(int, input('enter the numbers: ').split()))
ar = sorted(set(ar))
target = int(input('enter the target: '))
print(ar)

low = 0
high = len(ar) - 1
while high > low:
    mid = (high+low)//2
    if target > ar[mid]:
        low = mid + 1
    else:
        high = mid
print(f"the value {target} is at index {low} and in the position {low+1}!")
'''