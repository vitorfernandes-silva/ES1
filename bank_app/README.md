# Bank Application

Esta é uma aplicação simples de gerenciamento bancário implementada em Python. Ela contém as seguintes classes:

- **BankAccount**: Representa uma conta bancária com operações de depósito, saque e consulta de saldo.
- **Transaction**: Representa uma transação (depósito ou saque) executada em uma conta bancária.
- **Bank**: Gerencia várias contas bancárias e permite a realização de transferências entre contas.

# Estrutura do Projeto

    bank_app/
    ├── bank_app.py              # Código da aplicação
    ├── tests/
    │   ├── test_bank.py         # Testes para a classe Bank
    │   ├── test_bank_account.py # Testes para a classe BankAccount
    │   └── test_transaction.py  # Testes para a classe Transaction
    ├── Makefile                 # Arquivo Make para execução dos testes
    └── README.md                # Documentação e roteiro de execução


## Execução dos testes

Para executar os testes automatizados, siga os seguintes passos:

1. Clone o repositório
2. Execute os testes usando o Makefile (make test) ou alternativamente, execute: python -m unittest discover -s tests