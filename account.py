class Account:
    def __init__(self, name: str) -> None:
        '''
        Creates an account with a zero (0) balance

        :param name: Sets the account name
        '''
        self.__account_name = name
        self.__account_balance = 0.0
    
    def deposit(self, amount: float) -> bool:
        newAmount = self.__account_balance + amount
        if newAmount <= self.__account_balance:
            return False
        self.__account_balance = newAmount
        return True

    def withdraw(self, amount: float) -> bool:
        '''
        Decrements account balance fails when new balance is more than old
        :param amount: Change of account balance
        '''
        newAmount = self.__account_balance - amount
        if newAmount < 0 or newAmount >= self.__account_balance:
            return False
        self.__account_balance = newAmount
        return True

    def get_balance(self) -> float:
        '''
        Returns the current balance for the object
        '''
        return self.__account_balance
    def get_name(self) -> str:
        '''
        Returns the name for the object
        '''
        return self.__account_name