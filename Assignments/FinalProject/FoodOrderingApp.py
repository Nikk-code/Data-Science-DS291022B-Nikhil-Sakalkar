class Restaurant:
    
    def __init__(self, name):                       # ID, Food Name,  Quantity,  Discount,   Price,   Stock
        self.name=name
        self.food={1: {'Name': 'Chicken BiryanI', 'Quantity': 1, 'Price': 350.0, 'Discount': 80.0, 'Stock': 7.0}, 
                   2: {'Name': 'Kadia Chicken', 'Quantity': 5.0, 'Price': 200.0, 'Discount': 70.0, 'Stock': 6.0},
                   3: {'Name': 'Mutton Korma', 'Quantity': 1.0, 'Price': 420.0, 'Discount': 40.0, 'Stock': 10.0}, 
                   4: {'Name': 'Dahi Kabab', 'Quantity': 5.0, 'Price': 500.0, 'Discount': 30.0, 'Stock': 4.0},
                   5: {'Name': 'Italian Champ', 'Quantity': 1.0, 'Price': 420.0, 'Discount': 20.0, 'Stock': 3.0}, 
                   6: {'Name': 'Veg Noodle', 'Quantity': 1.0, 'Price': 100.0, 'Discount': 60.0, 'Stock': 4.0},
                   7: {'Name': 'Masala Chaap', 'Quantity': 1.0, 'Price': 90.0, 'Discount': 40.0, 'Stock': 7.0}, 
                   8: {'Name': 'Egg Curry', 'Quantity': 1.0, 'Price': 70.0, 'Discount': 50.0, 'Stock': 6.0},
                   9: {'Name': 'Spring Roll', 'Quantity': 2.0, 'Price': 260.0, 'Discount': 20.0, 'Stock': 7.0}, 
                   10: {'Name': 'Crispy Cord', 'Quantity': 1.0, 'Price': 200.0, 'Discount': 60.0, 'Stock': 6.0},
                   11: {'Name': 'Singapoori Noodle', 'Quantity': 1.0, 'Price': 380.0, 'Discount': 70.0, 'Stock': 7.0}, 
                   12: {'Name': 'Shawarma', 'Quantity': 2.0, 'Price': 320.0, 'Discount': 20.0, 'Stock': 5.0}}
        self.food_ID=len(self.food)+1
        self.user_details={1: {"User Name" : "Shruti", "Phone No." : 9433458729, "Email_ID" : 'shruti224@gmail.com', 'Password' : 'FREE FOOD', 'Address' : "Maharashtra"},
                           2: {"User Name" : "Aman", "Phone No." : 9874561238, "Email_ID" : 'aman@dummy.com', 'Password' : 'FREE FOOD', 'Address' : "Maharashtra"}}
        self.admin_details={1: {"Admin Name" : "Nikhil", "Phone No." : 8975836240, "Email_ID" : 'nikhil@dummy.com', 'Password' : 'FREE FOOD', 'Address' : "Maharashtra"}}
        
        self.ordered_item = []
        self.iterator=1
        

        
    # admin functionalities
    def admin_login(self):
        email=input("Enter Your Email ID : ")
        pas=input("Enter Your Password : ")
        while self.iterator <= (len(self.user_details)):
            if len(self.admin_details)!=0:
                if email==self.admin_details[self.iterator]["Email_ID"] and pas==self.admin_details[self.iterator]["Password"]:                    
                    print("\n"*4,"!! LOGIN SUCCESSFUL !!","\n"*2)
                    while True:
                        print("" * 31 + "ADMIN PAGE" + "" * 31 + "\n""\t(1) ADD FOOD / DRINKS\n""\t(2) EDIT SERVICES\n""\t(3) VIEW FOOD\n""\t(4) DELETE FOOD\n""\t(5) EXIT\n"+ "_" * 72)
                        y=input("\nYour choice: ")
                        if y=="1":
                            self.add_food_item()
                        elif y=="2":
                            self.edit_food_item()
                        elif y=="3":
                            self.view_food()
                        elif y=="4":
                            self.delete_food_item()
                        elif y=="5":
                            break
                        else:
                            print("\nInvalid Number")
                            break
                    break
                else:
                    print("INCORRECT  ADMIN DETAILS !!","\n"*4)
                    break
                    
            else:
                print("ADMIN LOGIN NOT POSSIBLE","\n"*4)
        
    def add_food_item(self):
        try:
            name=input("Enter the food name : ")
            quantity=float(input("Enter the quantity in values only : "))
            price=float(input("Enter the price in Rs only : "))
            discount=float(input("Enter the discount in Rs only : "))
            stock=float(input("Enter the available stock in values only : "))
            food_item={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item
            print("\n!! Food Item added successfully !!\n")
            print(""*25,"TOTAL ADDED ITEMS",""*20)
            
            self.view_food()
            
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n")
        
    def edit_food_item(self):
        print(""*25,"OUR MENU",""*20)

        self.view_food()
        
        try:
            x=int(input("Enter the Food ID you want to update : \n"))
            if x in self.food.keys():
                print("" * 31 + "ADMIN- EDIT PAGE" + "" * 31 + "\n""\t(1) UPDATE FOOD NAME\n""\t(2) UPDATE FOOD QUANTITY\n""\t(3) UPDATE FOOD PRICE\n""\t(4) UPDATE FOOD DISCOUNT\n""\t(5) UPDATE FOOD STOCK\n""\t(6) GO BACK\n"+ "_" * 72)
                y= input("Enter the number only : ")
                if y=="1":
                    self.food[x]["Name"]=input("Updated Food name : ")
                    print("\n!! Food Name Successfully Updated !!\n")
                elif y=="2":
                    self.food[x]["Quantity"]=float(input("Updated Quantity in values only : "))
                    print("\n!! Food Quantity Successfully Updated !!\n")
                elif y=="3":
                    self.food[x]["Price"]=float(input("Updated Price in Rs only : "))
                    print("\n!! Food Price Successfully Updated !!\n")
                elif y=="4":
                    self.food[x]["Discount"]=float(input("Updated Discount in Rs only : "))
                    print("\n!! Food Discount successfully Updated !!\n")
                elif y=="5":
                    self.food[x]["Stock"]=float(input("Updated Stock in values only : "))
                    print("\n!! Food Stock Successfully Updated !!\n")
                elif y=="6":
                    print("Back")
                else:
                    print("!! Sorry Invalid Number !!\n")
                
            else:
                print("\n!! Incorrect Food ID !!\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n")  
            
    def view_food(self):
        
        print("\n\n",""*25,"AVAILABLE FOOD ITEMS",""*20)
        print("\n\nFOOD ID|      FOOD ITEM    | QUANTITY | PRICE (₹) | DISCOUNT (₹)| STOCK (₹)")
        
        if len(self.food)!=0:
                menu=[]
                for items in self.food:
                    menu.append([items, self.food[items]["Name"], self.food[items]["Quantity"],self.food[items]["Price"], self.food[items]["Discount"], self.food[items]["Stock"]])
                for i in menu:
                    print("\n\n", i[0],"\t", i[1], " "*(20 - len(i[1])), i[2], "\t  ", i[3], "\t\t", i[4])
        
        else:
            print("!! Sorry No Food Items is Added !!\n")

    def delete_food_item(self):
        self.view_food()
        try:
            print(""*25,"!! WARNING !!",""*20)
            print('\n',' '*17,"Food Item will Delete Permanently",' '*10,"\n")
            print("Enter the Food ID ")
            x=int(input())
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print(""*25,"UPDATED FOOD LIST",""*20)
                self.view_food()
            else:
                print('\n',' '*17,"Incorrect food ID entered !",' '*10,"\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n")
                
                
    # USER FUNCTIONALIITY
                   
        
    def user_register(self):                      #User :    Username,  Phone no,   email,    Pass,   Address   
        try:
            i = len(self.user_details)
            while i >0:
                user_name=input("Enter your full name : ")
                phone_no=int(input("Enter your 10 digit phone number : "))
                email=input("Enter your email id : ")
                password=input("Enter your password : ")
                address=input("Enter your City:  ")
                for i in self.user_details.keys():           
                    if email==self.user_details[self.iterator]["Email_ID"]:
                        print("\n"*4,"YOU ALREADY HAVE AN ACCOUNT !")
                        print("\n"*4,"LOGIN FROM YOUR ACCOUNT or CREATE WITH NEW MAIL-ID !\n\n")
                        break
                        
                    else:
                        self.user_details[len(self.user_details)]={"User Name":user_name,"Phone No.":phone_no,"Email_ID":email,"Password":password,"Address":address}
                        print("\n!! Your Account is Created Successfully !!\n")
                        print(f"Welcome TO {self.name} Restaurant\n")
                        print(""*30,"USER DETAILS", ""*25)
                        for i in self.user_details[len(self.user_details)]:
                            print(i, ":", self.user_details[len(self.user_details)][i])
                        break
                break
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n ")      

    def user_login(self):
        try: 
            print(""*25,"WELCOME TO ",self.name,""*20)
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.user_details)!=0:
                for i in self.user_details.keys():           
                    if email==self.user_details[self.iterator]["Email_ID"] and pas==self.user_details[self.iterator]["Password"]:
                        print("\n"*4,"!! Login successful !!")
    #                     while True:
                        print("" * 31 + "USER ACCOUNT PAGE" + "" * 31 + "\n""\t(1) NEW ORDER \n""\t(2) MY HISTORY \n""\t(3) UPDATE PROFILE\n""\t(4) GO BACK\n"+ "_" * 72)
                        z=input("Enter Key : ")
                        if z=="1":
                            self.place_order()
                        elif z=="2":
                            self.ordered_history()
                        elif z=="3":
                            self.update_details()
                        elif z=="4":
                            print("Back")
                            break
                    elif  email==self.user_details[self.iterator]["Email_ID"]:
                        print("YOUR PASSWORD IS INCORRECT !")
                        break
                    elif (self.iterator==len(self.user_details)) and (email!=self.user_details[self.iterator]["Email_ID"] and pas!=self.user_details[self.iterator]["Password"]): 
                        print("YOU DONT HAVE AN ACCOUNT PLEASE CREATE ONE !\n\n\n")
                        break

                    else:
                        self.iterator += 1
        except :
            print("\n!! Something went wrong please try again !!")  

    def place_order(self):
#         payment=[]
        try:
            print("\n\nFOOD ID|      FOOD ITEM    | QUANTITY | PRICE (₹) | DISCOUNT (₹)")

            if len(self.food)!=0:
                    menu=[]
                    for items in self.food:
                        menu.append([items, self.food[items]["Name"], self.food[items]["Quantity"],self.food[items]["Price"], self.food[items]["Discount"]])
                    for i in menu:
                        print("\n\n", i[0],"\t", i[1], " "*(20 - len(i[1])), i[2], "\t", i[3], "\t\t", i[4])
            while True:
                print("" * 31  + "" * 31 + "\n""\t(1) PLACE ORDER \n""\t(2) PAYMENT \n""\t(3) GO BACK\n"+ "_" * 72)
                x=input("Your Key :")
                if x=="1":
                    print("Enter the Food number You want to order separated by comma")
                    y=input("You choice : ").split(",")
                    for i in y:
                        z=int(i)
                        if z<=len(menu):
                            self.ordered_item.append(menu[z-1])
                        else:
                            print("We Don't have this Food Item : ",z)
                            print(" Also make sure you include 'COMMAS' ! \for example: 1, 5, 9, 4'")
                            break
                    print("\n\n",""*25,"YOUR ORDER ", ""*20, "\n")
                    print("\n\nFOOD ID|      FOOD ITEM    | QUANTITY | PRICE (₹) | DISCOUNT (₹)")
                    payment=[]
                    for i in self.ordered_item:
#                         payment=[]
                        print("\n\n", i[0],"\t", i[1], " "*(20 - len(i[1])), i[2], "\t", i[3], "\t", i[4])
                        x=i[3]-i[4]
                        payment.append(x)
                    print("\n\n\t\tYour total payment is : ", sum(payment)," ₹")
                elif x=="2":
                    if len(self.ordered_item)==0:
                        print("Please make an order to pay")
                    else:
                        print("SUCCESSFULLY PAID ", sum(payment), " ₹")
                        exit()
                elif x=="3":
                    break
                else:
                    print("!! Invalid Number !!\n")

#         else:
#             print("\n!! Sorry! No Food Items are available Now !!\n")

        except :
            print("\n!! Something went wrong try again !!")     
                
    def ordered_history(self):
        print("\nList of Previous ordered : ")
        if len(self.ordered_item)==0:
            print("\n\nYOU DO NOT HAVE ANY ORDERS YET\n\n")
            
        else:
            for i in self.ordered_item:
                print("\n\n", i[0],"\t", i[1], " "*(20 - len(i[1])), i[2], "\t", i[3])
            
    def update_details(self):
        try:
            while True:
                print("Select Below Options to Update Your Profile Details\n")
                print("" * 31 + "EDIT PROFILE PAGE" + "" * 31 + "\n""\t(1) UPDATE NAME\n""\t(2) UPDATE PHONE NUMBER\n""\t(3) UPDATE EMAIL ID\n""\t(4) UPDATE PASSWORD\n""\t(5) UPDATE ADDRESS\n""\t(6) GO BACK\n"+ "_" * 72)
                
                print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit\n")
                x=input()
                if x=="1":
                    self.user_details["User Name"]=input("Enter your updated full name : ")
                    print("\n!! Detail Updated Successfully !!\n")
                elif x=="2":
                    self.user_details["Phone No."]=int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Detail Updated Successfully !!\n")      
                elif x=="3":
                    self.user_details["Email_ID"]=input("Enter your updated email id : ")
                    print("\n!! Detail Updated Successfully !!")
                    
                elif x=="4":
                    self.user_details["Password"]=input("Enter your updated password : ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="5":
                    self.user_details["Address"]=input("Enter your updated address with area PIN code ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")
                    
                if x in ["1","2","3",'4',"5"]:
                    for i in self.user_details:
                        print("Details Updated", i, ":",self.user_details[i])
                else:
                    print("\nPlease Enter correct Input\n")      
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n ")
            
            
       # CLASS EXECUTION BY CREATING INSTANCE

try:
    def main():
        instance= Restaurant("Ed_yoda-DA-Dhaba")
        print("" * 28, "WELCOME TO", instance.name, "" * 24, "\n")
        while True:
            print("\n\n\n","" * 31 + "MAIN MENU" + "" * 32 + "\n\n\n""\t(1) ADMIN\n""\t(2) USER\n""\t(3) EXIT\n" + "_" * 72)
            x=input("Please select your operation : ")
            if x=="1":
                print("\nDEAR ADMIN PLEASE LOGIN !\n")
                instance.admin_login()
            elif x=="2":
                while True:
                    print("\n\n",2,"" * 31 + "USER PAGE" + "*" * 31 + "\n\n""\t(1) CREATE ACCOUNT \n""\t(2) LOGIN \n""\t(3) EXIT\n"+ "_" * 72)
                    y=input("\nYour choice: ")
                    if y=="1":
                        instance.user_register()
                    elif y=="2":
                        instance.user_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")        
            elif x=="3":
                break
            else:
                print("Invalid Number")
except Exception as e:
    print("\n\nsomething went wrong please give input carefully")
            
        # calling the main function 
        
if __name__ =='__main__':
    main()

print("\n\nTHANK YOU EVERYONE !!\n\n")
