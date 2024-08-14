class Bank_of_nigeria:
    def __init__(self, first_name, last_name, age, address, hasAccount, checking_amount, savings_amount):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.hasAccount = hasAccount
        self.checkings_account = checking_amount
        self.saving_account = savings_amount
        self.investment_money = 2000

    def user_info(self):
        try:
            print(f'Users name: {self.last_name} Age: {self.age}, Address: {self.address}, Active Acount: {self.hasAccount}, Checking Account: {self.checkings_account} $, Savings Account: {self.saving_account} $, Investments Account: {self.investment_money} $')
        except Exception as e:
            print(e)

    def checking_account(self):
        print(f'Checking: {self.checkings_account} $')
        pass

    def savings_account(self):
        print(f'Savings: {self.saving_account} $')
        pass

    def add_money(self, amount):

        print(f"Now adding amount: {amount} $ ")
        self.checkings_account += amount
        return self.checkings_account

    def spend_money(self, amount):

        print(f"Now spending amount: {amount}$")
        self.checkings_account -= amount

    def transfer_money(self, amount):

        if amount <= self.checkings_account:
            self.checkings_account -= amount
            self.saving_account += amount
            print(f'You have transfered {amount}$ from your checking to your savings account')
        elif amount > self.checking_account:
            print('Insufficient funds')



darron_Account = Bank_of_nigeria('Darron', 'Dasher', 30, 'maryland', True, 500, 3000)

darron_Account.user_info()

darron_Account.add_money(1000)

darron_Account.checking_account()

darron_Account.transfer_money(500)

darron_Account.checking_account()