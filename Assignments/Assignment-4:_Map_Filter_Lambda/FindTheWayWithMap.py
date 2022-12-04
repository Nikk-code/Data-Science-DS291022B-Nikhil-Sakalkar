#Write a Python program to triple all numbers of a given list of integers. Use Python map.

lst = []
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
      
print("\nOriginal list: ")
print(lst)
result = map(lambda x: x * 3, lst) 
print("\nTriple of said list numbers:")
print(list(result))