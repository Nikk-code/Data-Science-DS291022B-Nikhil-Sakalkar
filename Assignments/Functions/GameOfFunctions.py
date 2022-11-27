#  Write a Python function to sum all the numbers in a list.
 
def sumInList(list1):
    total = 0
    for ele in range(0, len(list1)):
        total = total + list1[ele]
    print("\nSummation: ", total)

n = int(input("Enter number of elements : "))
  
# Below line read inputs from user using map() function 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
# print("\n", a)

sumInList(a)
