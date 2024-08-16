class Bank_Of_Nigeria: #Class for bank

    #Constructor for the class, takes in name, age and address. Sets default values for other parameters
    def __init__(self, name: str, age: int, address: str): 
        self.name = name
        self.age = age
        self.address = address
        self.verified_user = True
        self.money_in_checking = 0
        self.money_in_savings = 0
        self.investment_money = 50

    def get_user_info(self) -> None:

        print("~ Bank Of Nigeria ~") #Title of the bank
        print() #empty line, aesthetic purposes

        #try block to catch any errors that may occur
        try:

            #prints the user's information
            print(f'Users Name: {self.name}')
            print(f"Age: {self.age}")
            print(f"Address: {self.address}")
            print(f"Checking Account: {self.money_in_checking} $")
            print(f"Savings Account: {self.money_in_savings} $")
            print(f"Investments Account: {self.investment_money} $")
            print(f"Verified User: {self.verified_user}")

        except Exception as e:
            print(e) #prints the error that occurred.
            
        print()

    def get_financial_info(self):

        print("~ Bank Of Nigeria ~") #Title of the bank
        print()

        try:

            #prints the financial information specifically
            print(f"User {self.name}'s financial statement")
            print(f"Checking Account: {self.money_in_checking} $")
            print(f"Savings Account: {self.money_in_savings} $")
            print(f"Investments Account: {self.investment_money} $")

        except Exception as e:
            print(e) #prints the error that occurred.
            
        print()
        pass

        #Method to get the checking account information
    def get_checking_info(self):
        print(f'Checking: {self.money_in_checking} $')
        print()
        pass

        #Method to get the savings account information
    def get_savings_info(self):
        print(f'Savings: {self.money_in_savings} $')
        print()
        pass
    
    def deposit_money(self, amount: float):
        
        try:
            self.money_in_checking += amount #adds the amount to the checking account
            
            print(f"Successfully deposited {amount} $ to checking account for {self.name}")
            print()
            print(f"new checking total is: {self.money_in_checking}")
        except Exception as e:
            print(e)
            
        print()
            
        pass
    
    def withdraw_money(self, amount: float):
        
        try:
            self.money_in_checking -= amount #subtracts the amount from the checking account

            print(f"Successfully withdrew {amount} $ from checking account for {self.name}")
            print()
            print(f"new checking total is: {self.money_in_checking}")
        except Exception as e:
            print(e)
            
        print()
        
        pass
    
    def transfer_money(self, amount: float):
        
        try:
            if amount <= self.money_in_checking:
                
                print(f"Now transfering {amount} $ to savings account for {self.name}")
                
                self.money_in_checking -= amount #subtracts the amount from the checking account
                self.money_in_savings += amount  #adds the amount to savings account
                
                self.get_checking_info() #calls the updated checking account information
                self.get_savings_info() #calls the updated savings account information
                
                print()
                print(f"Successfully transferred {amount} $ from checking account to savings account for {self.name}")
            else:
                print("Insufficient funds in checking account")
        except Exception as e:
            print(e)
            
        print()
        
        pass
        

Darron_Account = Bank_Of_Nigeria('Darron Nigwo', 5, '1205 lifton ave, Banana Island, Lagos, Nigeria')

Darron_Account.deposit_money(400)

Darron_Account.get_user_info()