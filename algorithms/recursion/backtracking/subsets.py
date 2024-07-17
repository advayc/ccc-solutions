def search(items, final, subset, index):
    final.append(subset[:]) # dupe whats currently in subset into final

    for i in range(index, len(items)):
        subset.append(items[i]) # add all items into the subset
        search(items, final,subset,i+1) # go to the next element 
        subset.pop() 
    return final

print(search([1, 2, 3],[],[],0))