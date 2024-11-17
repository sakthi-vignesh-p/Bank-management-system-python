import random

class customer :#Custemer class
     
     def __init__(self,UserName,UserAge,UserGender,userPassword): # Constructor to set user details
           
           #User names and Additional details
           self.name=UserName 
           self.age=UserAge
           self.gender=UserGender
           self.accountPassword=userPassword
           self.balance=0
           random_integer="" #Temprory variable to create random number
           #Create a 10 digit account number
           for i in range(1,11,1):
            random_integer += str(random.randint(1, 9))
           #declare the random 10 digit number as customer accountNumber
           self.accountNumber=random_integer

     #Display function to show customer details
     def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}") 
        print(f"Account Number: {self.accountNumber}") 
     
     #withdrawl function
     def withdrawl_amount(self,amount):
          if(self.balance<amount):#check balance  
             print("No Balance")
             return None
          else:
            self.balance-=amount #subract the withdrawl amount from balance
            print(f"withdrawl amount :{amount}")
            return amount

     #Deposit function
     def deposit_amount(self,amount):
         self.balance+=amount    
         print(f"Deposited : {amount}")

      #check balance
     def show_balance(self):
         print(f"Available Balance: {self.balance}")
          