import customer #import customer.py module
customers=customer.customer #get customer class from module and store it on customers

def line():
   print("-------------------------------------")

customersList=[] #to store account holders
loop=True #loop the code

while(loop): #looping the program
      line()
      print("*  Login Acount   --> 1") # 1 to login
      print("* Create Account  --> 2") #2 to create a new account
      line()

      option=int(input()) #Get user option
      
      if(option==0 or option>2):#check user option 
            print("Invalid option only (1,2) is valid")
            continue #return to the next iteration on invalid option
      
      if(option==1):
          #ask user name to find the account
          line()
          name=input("Enter Name : ")
          currentCustomer=None #temprory variable to check name is valid or not
          #check the name is already taken or not
          for i in customersList:
            if(name==i.name):
                 currentCustomer=i

          if(currentCustomer==None):    
             print("No Account found")
             continue #if name is already exist return to the next iteration
          
          password=int(input("Enter password : "))

          if(currentCustomer.accountPassword !=password):
              print("Incorrect password")
              continue
          line()  
        
          #Ask user option
          print("* Withdrawl       --> 1")
          print("* Deposit         --> 2")
          print("* Check Balance   --> 3") 
          print("* Main menu       --> 0") 
          line()
          
          opt=int(input()) #Get user option

          if(opt==0):
           continue
          
          if(opt>3):#check user option 
            print("Invalid option only (1,2,3) is valid")
            continue #return to the next iteration on invalid option

         #withdrawl function
          if(opt==1):
            line()
            amount=int(input("Enter withdrwal amount : "))
            #check avalialabe balance
            amount=currentCustomer.withdrawl_amount(amount)#temprory variable to check balance
             #if no balance return to the next iteration
            if(amount==None):
             continue
            #check balance after withdrawl
            line()
            opt=int(input("Enter 1 to check balance or 0 to exit"))
            if(opt==1):
             #print avalailable balance and return to the next iteration
             print(f"Availabe balance is : {currentCustomer.balance }")  
             continue

          #deposit function
          if(opt==2): 
             #get deposit amount from user
             line()
             amount=int(input("Enter Amount to deposit : "))
             currentCustomer.deposit_amount(amount)
              
          line()
          opt=int(input("Enter 1 to check balance or 0 to exit"))
          if(opt==1):
            print(f"Availabe balance is : {currentCustomer.balance }")  
            continue
          #show balance
          if(opt==3):
            print(f"Availabe balance is : {currentCustomer.balance }")  
            continue 

      #create a new account
      if(option==2): 
         line()
         name=input("Enter name : ")
         n=None
         for i in customersList:
             if(name==i.name):
                print("Name already exist")
                n=name
                break

         if(n !=None)  :
              continue 

         line()

         age=int(input("Enter your age : "))

         if(age==0 or age>110):
               print("Invalid age")
               continue 
         line()
         gender=input("Enter gender (M,F,O) : ")
         if(gender != "M" and gender !="F" and gender !="O"):
             print("Only M,F,O is valid")
             continue 
         line()
         passWrd=int(input("Enter a 4 digit password : "))
         passWrd=str(passWrd)
      
         if(len(passWrd)<4 or len(passWrd)>4):
            print("Password must be in 4 digit : ")
            continue 
         customers=customer.customer(name,age,gender,int(passWrd)) #create a new customer object
         customersList.append(customers)
         line()
         print("Account created succesfully")
         line()
         customers.display_details()      
         line()