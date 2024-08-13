class Bank_of_nigeria:
    def __init__(self, first_name, last_name, age, address, hasAccount, amount, amount_savings):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.hasAccount = hasAccount
        self.amount = amount
        self.amount_savings = amount_savings
        self.investment_money = 2000

    def user_info(self):
        try:
            print(f'Users name: {self.last_name} Age: {self.age}, Address: {self.address}, Active Acount: {self.hasAccount}, Checking Account: {self.amount} $, Savings Account: {self.amount_savings} $, Investments Account: {self.investment_money} $')
        except Exception as e:
            print(e)

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


Tobi_Account = Bank_of_nigeria('Darron', 'Dasher', 30, 'maryland', True, 200, 3000)

Tobi_Account.user_info()

Tobi_Account.add_money(300)

Tobi_Account.checking_account()

Tobi_Account.spend_money(30)

Tobi_Account.checking_account()

Tobi_Account.user_info()

print("what is your name: ")

Input = input()

print(f"hello {Input}")

#adding a new comment section to solve this git prpoblem aiuornhoieauhgoauehgorvuahvkaorpkavrvfaer