# tests/test_bank.py

import unittest
from bank_app import Bank, BankAccount

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.account1 = BankAccount("Alice", 100.0)
        self.account2 = BankAccount("Bob", 50.0)
        self.bank.add_account(self.account1)
        self.bank.add_account(self.account2)

    def test_add_existing_account(self):
        with self.assertRaises(ValueError):
            self.bank.add_account(BankAccount("Alice", 200.0))

    def test_get_account_not_found(self):
        with self.assertRaises(ValueError):
            self.bank.get_account("Charlie")

    def test_transfer_valid(self):
        self.bank.transfer("Alice", "Bob", 70.0)
        self.assertEqual(self.account1.get_balance(), 30.0)
        self.assertEqual(self.account2.get_balance(), 120.0)

    def test_transfer_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.bank.transfer("Alice", "Bob", -10)

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.bank.transfer("Bob", "Alice", 100)

if __name__ == '__main__':
    unittest.main()
