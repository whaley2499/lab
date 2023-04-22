import unittest as utest
from account import *

class TestAccount(utest.TestCase):
    
    def setUp(self):
        self.account1 = Account("John")
        self.account2 = Account("Jane")
        self.account2.deposit(100.00)

    def tearDown(self):
        del self.account1
        del self.account2
    
    def test_init(self):
        self.assertEqual(self.account1.get_name(), 'John')
    
    def test_deposit(self):
        self.assertFalse(self.account1.deposit(-1))
        self.assertEqual(self.account1.get_balance(), 0)

        self.assertFalse(self.account1.deposit(0))
        self.assertEqual(self.account1.get_balance(), 0)

        self.assertTrue(self.account1.deposit(1))
        self.assertEqual(self.account1.get_balance(), 1)

        self.assertTrue(self.account1.deposit(1.01))
        self.assertEqual(self.account1.get_balance(), 2.01)

        self.assertRaises(TypeError, self.account1.deposit, 'one')

    def test_withdraw(self):
        self.assertFalse(self.account1.withdraw(-1))
        self.assertEqual(self.account1.get_balance(), 0)

        self.assertFalse(self.account1.withdraw(0))
        self.assertEqual(self.account1.get_balance(), 0)

        self.assertFalse(self.account1.withdraw(100))
        self.assertEqual(self.account1.get_balance(), 0)

        self.assertTrue(self.account2.withdraw(1))
        self.assertEqual(self.account2.get_balance(), 99)

        self.assertTrue(self.account2.withdraw(50.00))
        self.assertEqual(self.account2.get_balance(), 49)

        self.assertTrue(self.account2.withdraw(49))
        self.assertEqual(self.account2.get_balance(), 0)

        self.assertRaises(TypeError, self.account1.withdraw, 'one')
    
    def test_get_balance(self):
        self.assertEqual(self.account2.get_balance(), 100)
        self.assertNotEqual(self.account2.get_balance(), 0)
    
    def test_get_name(self):
        self.assertEqual(self.account1.get_name(), "John")
        self.assertNotEqual(self.account1.get_name(), "Jane")

if __name__ == '__main__':
    utest.main()