class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0.0
    
    def deposit(self, amount):
        newAmount = self.__account_balance + amount
        if newAmount <= self.__account_balance:
            return False
        self.__account_balance = newAmount
        return True

    def withdraw(self, amount) :
        newAmount = self.__account_balance - amount
        if newAmount < 0 or newAmount >= self.__account_balance:
            return False
        self.__account_balance = newAmount
        return True

    def get_balance(self):
        return self.__account_balance
    def get_name(self):
        return self.__account_name