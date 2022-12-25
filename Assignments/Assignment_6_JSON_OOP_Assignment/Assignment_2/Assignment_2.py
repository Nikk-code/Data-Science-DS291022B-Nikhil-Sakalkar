class Dog:
    def __init__(self,name,age,coat_colour):
        self.name = name
        self.age = age
        self.coat_colour = coat_colour
    
    def description(self):
        print(f"Name : {self.name} \nAge : {self.age}")

    def get_info(self):
        print(f"Coat Colour : {self.coat_colour}")

class JackRussellTerrier(Dog):
    def __init__(self,name,age,coat_colour,life,owner):
        super().__init__(name,age,coat_colour)
        self.life = life
        self.owner = owner
    
    def display(self):
        print(f"Life of dog : {self.life} years")
        print(f"Owner : {self.owner} \n" )
        
class Bulldog(Dog):
    def __init__(self,name,age,coat_colour, life ,nickname):
        super().__init__(name,age,coat_colour)
        self.life = life
        self.nickname = nickname

    def display(self):
        print(f"Life of dog : {self.life} years")
        print(f"Nick name : {self.nickname}")

print("**********Calling JackRussellTerrier**********")
jackRussellTerrier = JackRussellTerrier("Tommy",5,"White", 15 ,"Nikhil")
jackRussellTerrier.description()
jackRussellTerrier.get_info()
jackRussellTerrier.display()

print("**********Calling Bulldog**********")
bulldog = Bulldog("Luna",3,"Brown", 10, "Jack")
bulldog.description()
bulldog.get_info()
bulldog.display()
