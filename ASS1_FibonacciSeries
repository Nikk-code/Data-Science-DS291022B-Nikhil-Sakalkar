# Write a Python program to get the Fibonacci series between 0 to 50

nth = int(input("Enter number: "))
n1, n2 = 0, 1
count = 0

# checking numbers are valid
if nth <= 0 or nth > 50:
   print("Please enter a number between 1 to 50")

elif nth == 1:
   print("Fibonacci series upto",nth,":", n1)

else:
   print("Fibonacci series:")
   while count < nth:
       print(n1)
       x = n1 + n2
       n1 = n2
       n2 = x
       count += 1
