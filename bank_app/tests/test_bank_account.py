# tests/test_bank_account.py

import unittest
from bank_app import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("João", 100.0)

    def test_deposit_valid(self):
        self.account.deposit(50.0)
        self.assertEqual(self.account.get_balance(), 150.0)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw_valid(self):
        self.account.withdraw(30.0)
        self.assertEqual(self.account.get_balance(), 70.0)

    def test_withdraw_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-20)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == '__main__':
    unittest.main()
