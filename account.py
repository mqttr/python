class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0.0
    
    def deposit(self, amount):
        newBalance = self.__account_balance + amount
        if newBalance <= self.__account_balance:
            return False
        self.__account_balance = newBalance
        return True

    def withdraw(self, amount) :
        newBalance = self.__account_balance - amount
        if newBalance < 0 or newBalance >= self.__account_balance:
            return False
        self.__account_balance = newBalance
        return True

    def get_balance(self):
        return self.__account_balance
    def get_name(self):
        return self.__account_name