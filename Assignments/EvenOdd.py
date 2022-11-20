# Write a Python program to count the number of even and odd numbers from a series of numbers.

seriesOfNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

evenCount = 0
oddCount = 0

for i in seriesOfNumbers:
    if not i % 2:
        evenCount+=1
    else:
    	oddCount+=1
print("Number of even numbers :",evenCount)
print("Number of odd numbers :",oddCount)
