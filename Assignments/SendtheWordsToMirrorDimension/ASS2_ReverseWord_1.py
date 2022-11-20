# Write a Python program that accepts a word from the user and reverse it.

word = input("Input a word to reverse: ")
str = ""

print("The original string is : ", end="")
print(word)

for i in word:
  str = i + str
print(str)
