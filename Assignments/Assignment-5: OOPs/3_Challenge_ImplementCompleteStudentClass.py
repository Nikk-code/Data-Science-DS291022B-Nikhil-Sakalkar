# Challenge 3: Implement the Complete Student Class

class Student:
    def student(self,name,rollnumber):
        self.__name = name                       # made name a private member
        self.__rollnumber = rollnumber           # made rollnumber a private number

    def setName(self,name):
        self.__name = name
    def getName(self):
        return f"Name of Student : {self.__name}"

    
    def setRollNumber(self,rollnumber):
        self.__rollnumber = rollnumber
    def getRollNumber(self):
        return f"Roll number of Student : {self.__rollnumber}"

StudentName = input("Enter student name: ")
StudentRollNo = input("Enter student roll number: ")

student = Student()
student.setName(StudentName)
data = student.getName()
print(data)
student.setRollNumber(StudentRollNo)
data = student.getRollNumber()
print(data)
