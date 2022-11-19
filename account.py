def __init__(self, name):
    __account_name__ = name
    __account_balance__ = 0


def deposit(self, amount):
    requested_balance = self.__account_balance__ + amount

    if requested_balance > 0 and amount > 0:
        self.__account_balance__ = requested_balance
        return True
    else:
        return False


def withdraw(self, amount):
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
