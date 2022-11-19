class Account:
    def __init__(self, name):
        """
        Initialises the account as an object stored in memory.

        :param name: of the account holder; please note that this cannot be changed unless new account is made
        :return: None
        """
        self.__account_name__ = name
        self.__account_balance__ = 0


    def deposit(self, amount):
        """
        Adds numeric amount to the account's balance.

        :param amount: Positive numeric amount of currency to deposit into account
        :return: Boolean indicating whether the account change was successful
        """

        try:
            amount = float(amount)
        except (ValueError, TypeError):
            return False

        requested_balance = self.__account_balance__ + amount

        if requested_balance > 0 and amount > 0:
            self.__account_balance__ = requested_balance
            return True
        else:
            return False


    def withdraw(self, amount):
        """
        Deducts amount from the account's balance.

        :param amount: Positive numeric amount of currency to withdraw from account
        :return: Boolean indicating whether the account change was successful
        """

        try:
            amount = float(amount)
        except (ValueError, TypeError):
            return False

        requested_balance = self.__account_balance__ - amount

        if requested_balance > 0 and amount > 0:
            self.__account_balance__ = requested_balance
            return True
        else:
            return False


    def get_balance(self):
        return self.__account_balance__


    def get_name(self):
        return self.__account_name__
