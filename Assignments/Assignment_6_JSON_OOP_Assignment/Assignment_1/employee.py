import json

class Employees:
    def __init__(self,name,dob,height,city,state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Open a json file
with open('employee.json','r') as file :
    data = json.load(file)
    
# Create a list of Employee object from the dict
employees = [Employees(e['Name'], e['DOB'], e['Height'], e['City'] , e['State']) for e in data['Employees']]

# Printing the list
for employee in employees:
    print("Name: ", employee.name) 
    print("DOB: ", employee.dob) 
    print("Height: ", employee.height) 
    print("City: ", employee.city) 
    print("State: ", employee.state) 
    print("\n")
