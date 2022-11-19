import account
from unittest import TestCase
from random import uniform


class Test(TestCase):

    def test_init_pass(self):
        self.name = "test"
        self.test = account.Account(self.name)
        assert self.test.get_name() == self.name
        assert self.test.get_balance() == 0

    def test_init_mismatch_fail(self):
        self.name = "test"
        self.test = account.Account(self.name)

        self.name = "different"
        assert not self.test.get_name() == self.name
        assert not self.test.get_balance() == 1

    def test_deposit_pass(self):
        self.name = "test"
        self.amount = uniform(.01, 1)
        self.test = account.Account(self.name)
        assert self.test.deposit(self.amount) == True
        assert self.test.get_balance() == self.amount

    def test_deposit_mismatch_fail(self):
        self.name = "test"
        self.amount = uniform(.01, 1)
        self.test = account.Account(self.name)
        assert self.test.deposit(self.amount) == True

        self.amount *= -1  # Inverting random amount
        assert not self.test.get_balance() == self.amount

    def test_deposit_zero_fail(self):
        self.name = "test"
        self.amount = 0
        self.test = account.Account(self.name)
        assert self.test.deposit(self.amount) == False

    def test_deposit_negative_fail(self):
        self.name = "test"
        self.amount = -1 * uniform(.01, 1)
        self.test = account.Account(self.name)
        assert self.test.deposit(self.amount) == False

    def test_deposit_nonnumeric_fail(self):
        self.name = "test"
        self.amount = self.name
        self.test = account.Account(self.name)
        self.test.deposit(self.amount)
        assert self.test.deposit(self.amount) == False

    def test_withdraw_pass(self):
        self.name = "test"
        self.balance = 1
        self.amount = uniform(.01, 1)
        self.test = account.Account(self.name)
        assert self.test.deposit(self.balance) == True
        assert self.test.withdraw(self.amount) == True
        assert self.test.get_balance() == (self.balance - self.amount)

    def test_withdraw_mismatch_fail(self):
        self.name = "test"
        self.balance = 1
        self.amount = uniform(.01, 1)
        self.test = account.Account(self.name)
        assert self.test.deposit(self.balance) == True

        self.amount *= -1  # Inverting random amount
        assert not self.test.get_balance() == self.amount

    def test_withdraw_negative_fail(self):
        self.name = "test"
        self.balance = 1
        self.amount = -1 * uniform(.01, 1)
        self.test = account.Account(self.name)
        assert self.test.deposit(self.balance) == True
        assert self.test.withdraw(self.amount) == False

    def test_withdraw_zero_fail(self):
        self.name = "test"
        self.balance = 1
        self.amount = 0
        self.test = account.Account(self.name)
        assert self.test.deposit(self.balance) == True
        assert self.test.withdraw(self.amount) == False

    def test_withdraw_nonnumeric_fail(self):
        self.name = "test"
        self.balance = 1
        self.amount = self.name
        self.test = account.Account(self.name)
        assert self.test.deposit(self.balance) == True
        assert self.test.withdraw(self.amount) == False
