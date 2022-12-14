#  Challenge 1: Square Numbers and Return Their Sum

class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        square_sum = (self.x**2)+(self.y**2)+(self.z**2)
        return square_sum

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

point = Point(x,y,z)
data = point.sqSum()
print(data)
