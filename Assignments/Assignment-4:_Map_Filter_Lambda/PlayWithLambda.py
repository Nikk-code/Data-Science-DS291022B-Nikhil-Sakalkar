#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

Add = lambda a : a +25
x = int(input("Enter number: "))
print("Addition of", x, "+ 25 = ",Add(x))
