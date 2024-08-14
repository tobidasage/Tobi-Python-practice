class Bank_Of_Nigeria: #Class for bank

    #Constructor for the class, takes in name, age and address. Sets default values for other parameters
    def __init__(self, name, age, address): 
        self.name = name
        self.age = age
        self.address = address
        self.verified_user = True
        self.money_in_checking = 0
        self.money_in_savings = 0
        self.investment_money = 50

    def user_info(self):

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

    def checking_account(self):
        print(f'Checking: {self.amount} $')
        pass

    def savings_account(self):
        print(f'Savings: {self.amount_savings} $')
        pass

    def add_money(self, amount):
        self.amount += amount
        return self.amount

    def spend_money(self, amount):
        self.amount -= amount


Bank_Account = Bank_Of_Nigeria('Darron Nigwo', 5, '1205 lifton ave, Banana Island, Lagos, Nigeria')

Bank_Account.user_info()
