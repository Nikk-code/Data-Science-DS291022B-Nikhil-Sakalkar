# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def UpperLowerCase(s):
   d={"UPPER_CASE":0, "LOWER_CASE":0}
   for c in s:
      if c.isupper():
         d["UPPER_CASE"]+=1
      elif c.islower():
         d["LOWER_CASE"]+=1
      else:
         pass

   print ("No. of Upper case characters : ", d["UPPER_CASE"])
   print ("No. of Lower case Characters : ", d["LOWER_CASE"])
   
x = input("Enter string: ")
print("\nOriginal string: ", x)
UpperLowerCase(x)
