class Account():

    def __init__(self, name:str) -> None:
        '''
        This function initializes an account object

        :param name: Account name
        '''
        self.__account_name = name
        self.__account_balance = 0.00
    
    def deposit(self, amount:float) -> bool:
        '''
        This function takes a value and increments the balance of the account.

        :param amount: This is the amount to add to the account.
        :return: True on success. False if given a value of zero or less.
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount:float) -> bool:
        '''
        This function takes a value and reduces the account balnce.

        :param amount: This is the amount to reduce the account by.
        :return: True on success. False if given a value of zero or a value larger than the account's balance 
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    def get_balance(self) -> float:
        '''
        This function gets the account's balance

        :param None:
        :return: The value of account_balance
        '''
        return float(self.__account_balance)
    
    def get_name(self) -> str:
        '''
        This function gets the name of the account holder.

        :param None:
        :return: The value of account_name
        '''
        return self.__account_name