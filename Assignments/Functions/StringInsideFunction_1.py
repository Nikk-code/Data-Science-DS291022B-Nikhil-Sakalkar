# Write a Python program to reverse a string.

def ReverseString(x):
    return x[::-1]

x = input("Enter string: ")
print("\nOriginal string: ", x)
a = ReverseString(x)
print("\nReversed string: ", a)
