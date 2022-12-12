# Challenge 2: Implement a Calculator Class

class cal():
   def __init__(self,in_1,in_2):
      self.a=in_1
      self.b=in_2
   def add_vals(self):
      return self.a+self.b
   def multiply_vals(self):
      return self.a*self.b
   def divide_vals(self):
      return self.a/self.b
   def subtract_vals(self):
      return self.a-self.b

a = input("Enter the first number: ")
b = input("Enter the second number: ")
print("The entered first and second numbers are : ")
print(a, b)

obj = cal(a,b)
choice=1
while choice!=0:
   print("0. Exit")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   choice=int(input("Enter your choice... "))
   if choice==1:
      print("The computed addition result is : ",obj.add_vals())
   elif choice==2:
      print("The computed subtraction result is : ",obj.subtract_vals())
   elif choice==3:
      print("The computed product result is : ",obj.multiply_vals())
   elif choice==4:
      print("The computed division result is : ",round(obj.divide_vals(),2))
   elif choice==0:
      print("Exit")
   else:
      print("Sorry, invalid choice!")
print()
