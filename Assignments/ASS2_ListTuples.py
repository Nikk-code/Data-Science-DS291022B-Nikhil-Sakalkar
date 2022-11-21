# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

x = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("List of Tuple before sorting : " + str(x))

listLen = len(x); 
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(x[j][-1] > x[j + 1][-1]):
            swap = x[j]
            x[j] = x[j + 1]
            x[j + 1] = swap

print("List of Tuple after sorting : " + str(x))
