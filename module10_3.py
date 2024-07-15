import threading
from threading import Thread


class BankAccount(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 1000
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                return "Insufficient funds"


def deposit_task(account, amount):
    for i in range(5):
        new_balance = account.deposit(amount)
        print(f'{threading.current_thread().name}: {amount}, new balance is {new_balance}')


def withdraw_task(account, amount):
    for i in range(5):
        result = account.withdraw(amount)
        if isinstance(result, int):
            print(f'{threading.current_thread().name}: {amount}, new balance is {result}')
        else:
            print(f'{threading.current_thread().name}: {result}')


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100), name="Deposit")
withdraw_thread = Thread(target=withdraw_task, args=(account, 150), name="Withdraw")

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
