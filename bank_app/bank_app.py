# bank_app.py

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente.")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class Transaction:
    def __init__(self, account, transaction_type, amount):
        if transaction_type not in ['deposit', 'withdraw']:
            raise ValueError("Tipo de transação inválido.")
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

    def execute(self):
        if self.transaction_type == 'deposit':
            self.account.deposit(self.amount)
        elif self.transaction_type == 'withdraw':
            self.account.withdraw(self.amount)


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_holder in self.accounts:
            raise ValueError("Conta já existe.")
        self.accounts[account.account_holder] = account

    def get_account(self, account_holder):
        if account_holder not in self.accounts:
            raise ValueError("Conta não encontrada.")
        return self.accounts[account_holder]

    def transfer(self, from_holder, to_holder, amount):
        if amount <= 0:
            raise ValueError("O valor da transferência deve ser positivo.")
        from_account = self.get_account(from_holder)
        to_account = self.get_account(to_holder)
        if from_account.get_balance() < amount:
            raise ValueError("Saldo insuficiente para transferência.")
        from_account.withdraw(amount)
        to_account.deposit(amount)
