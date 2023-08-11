class Account:
    def __init__(self, name: str) -> None:
        '''
        Creates an account with a zero (0) balance

        :param name: Account's name
        '''
        self.__account_name = name
        self.__account_balance = 0.0
    
    def deposit(self, amount: float) -> bool:
        '''
        Method to deposit funds from an account.

        :param amount: Amount to be deposited
        :return: True if deposit is successful; False if deposit is unsuccessful
        '''
        newBalance = self.__account_balance + amount
        if newBalance <= self.__account_balance:
            return False
        self.__account_balance = newBalance
        return True

    def withdraw(self, amount: float) -> bool:
        '''
        Method to withdraw funds from an account

        :param amount: Amount to be withdrawn
        :return: True if withdraw is successful; False if withdraw is unsuccessful
        '''
        newBalance = self.__account_balance - amount
        if newBalance < 0 or newBalance >= self.__account_balance:
            return False
        self.__account_balance = newBalance
        return True

    def get_balance(self) -> float:
        '''
        Method gets the current balance of the account

        :return: Account's current balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method gets the user's name of the account

        :return: Account's current name
        '''
        return self.__account_name
