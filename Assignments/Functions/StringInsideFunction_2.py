# Write a Python program to reverse a string.

def ReverseString(x):
    str = ""
    for i in x:
        str = i + str
    return str

x = input("Enter string: ")
print("\nOriginal string: ", x)
a = ReverseString(x)
print("\nReversed string: ", a)
