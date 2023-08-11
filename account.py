class Account:
    def __init__(self, name: str) -> None:
        '''
        Creates an account with a zero (0) balance

        :param name: Account's user's name
        '''
        self.__account_name = name
        self.__account_balance = 0.0
    
    def deposit(self, amount: float) -> bool:
        '''
        Method decrements account balance. It fails when new balance is less than previous balance or amount is <= 0.

        :param amount: Increments balance by amount
        :return: True/False depending on success of withdraw
        '''
        newBalance = self.__account_balance + amount
        if newBalance <= self.__account_balance:
            return False
        self.__account_balance = newBalance
        return True

    def withdraw(self, amount: float) -> bool:
        '''
        Method increments account balance. It fails when new balance is more than previous balance or amount is <= 0.

        :param amount: Decrements balance by amount
        :return: True/False depending on success of withdraw
        '''
        newBalance = self.__account_balance - amount
        if newBalance < 0 or newBalance >= self.__account_balance:
            return False
        self.__account_balance = newBalance
        return True

    def get_balance(self) -> float:
        '''
        Method gets the current balance of the account

        :return: Account User's current balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method gets the user's name of the account

        :return: Account User's full name
        '''
        return self.__account_name
