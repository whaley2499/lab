import pytest as pt
from account import *

class Test:

    def setup_method(self):
        self.account1 = Account("John")
        self.account2 = Account("Jane")
        self.account2.deposit(100.00)
    
    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'John'

    def test_deposit(self):
        assert self.account1.deposit(-1) == False
        assert self.account1.get_balance() == 0
        
        assert self.account1.deposit(0) == False
        assert self.account1.get_balance() == 0

        assert self.account1.deposit(1) == True
        assert self.account1.get_balance() == 1

        assert self.account1.deposit(1.01) == True
        assert self.account1.get_balance() == 2.01

        pt.raises(TypeError, self.account1.deposit, 'one')
    
    def test_withdraw(self):
        assert self.account1.withdraw(-1) == False
        assert self.account1.get_balance() == 0

        assert self.account1.withdraw(0) == False
        assert self.account1.get_balance() == 0

        assert self.account1.withdraw(100) == False
        assert self.account1.get_balance() == 0

        assert self.account2.withdraw(1)
        assert self.account2.get_balance() == 99

        assert self.account2.withdraw(50.10)
        assert self.account2.get_balance() == 48.90

        assert self.account2.withdraw(48)
        assert self.account2.get_balance() == pt.approx(0.90, abs=0.001)

        pt.raises(TypeError, self.account2.withdraw, "two")
    
    def test_get_balance(self):
        assert self.account2.get_balance() == 100
        assert self.account1.get_balance() != 100

    def test_get_name(self):
        assert self.account1.get_name() == "John"
        assert self.account2.get_name() != "John"

if __name__ == '__main__':
   retcode = pt.main()