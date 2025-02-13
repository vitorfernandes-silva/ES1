# tests/test_transaction.py

import unittest
from bank_app import BankAccount, Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Maria", 100.0)

    def test_deposit_transaction(self):
        transaction = Transaction(self.account, 'deposit', 50.0)
        transaction.execute()
        self.assertEqual(self.account.get_balance(), 150.0)

    def test_withdraw_transaction(self):
        transaction = Transaction(self.account, 'withdraw', 30.0)
        transaction.execute()
        self.assertEqual(self.account.get_balance(), 70.0)

    def test_invalid_transaction_type(self):
        with self.assertRaises(ValueError):
            Transaction(self.account, 'invalid', 10)

    def test_withdraw_insufficient_funds(self):
        transaction = Transaction(self.account, 'withdraw', 200)
        with self.assertRaises(ValueError):
            transaction.execute()

if __name__ == '__main__':
    unittest.main()
