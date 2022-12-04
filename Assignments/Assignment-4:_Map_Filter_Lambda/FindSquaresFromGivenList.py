# Write a Python program to square the elements of a list using map() function.

lst = []
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
      
print("\nOriginal list: ")
print(lst)
result = map(lambda x: x * 2, lst) 
print("\nSquare of said list numbers:")
print(list(result))