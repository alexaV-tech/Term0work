class House:
    #varibles in classes are attributes
    numOfDoors=0
    furniture=[]
    isLocked= True

alexaHouse= House()
alexaHouse.numOfDoors=7
#this just calls out the. varibles inside 
print(alexaHouse.numOfDoors)

class Pet:
    #constructor(these varibles can be used throughout the class)
    def __init__(self, name, age, hasLegs):
        self.name= name
        self.age=age
        self.hasLegs= hasLegs
        #example of it being used in a method 
    def intro(self):
        print(self.name, "is", self.age, "years old")

cat1= Pet("zuzu", 3, True)
cat1.intro() # a method should be called along with the dot attached to the object
    

#get pin
#deposit
#view
#take out(withdraw)

class BankAccount:
    def __init__(self, name, balance, pin): 
        self.name = name
        self.balance = balance
        self.pin = pin
    
    def subtract(self, amount):
        self.balance -= amount  

    def addition(self, amount):
        self.balance += amount  
    
    def view(self):
        print(self.balance)


class ATM:
    def __init__(self, pin, action, bank_account):  # Added bank_account instance in order to call
        self.pin = pin
        self.action = action
        self.bank_account = bank_account # Store the bank account instance
   
    def checker(self):
        pins = [1234, 6778, 9989, 0000]
        if self.pin in pins:
            return True
      #put self if you wanna use methods within the class
    def actionSending(self):
        if self.checker():
            if self.action == "withdraw":
                x = float(input("How much will you be withdrawing")) 
                self.bank_account.subtract(x) # Call method on bank_account instance
            if self.action == "deposit":
                x = float(input("How much will you be depositing")) 
                self.bank_account.addition(x)
            if self.action == "view":
                self.bank_account.view() 

my_account = BankAccount("Alexa", 1000, 1234)
atm_withdraw = ATM(1234, "withdraw", my_account)
atm_view = ATM(1234, "view", my_account)
atm_withdraw.actionSending()
atm_view.actionSending()




        



    



