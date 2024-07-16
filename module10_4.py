from queue import Queue
from threading import Thread, Lock
from time import sleep
from datetime import datetime
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer:
    def __init__(self, number):
        self.number = number


class Cafe:
    def __init__(self, num_tables):
        self.tables = [Table(i) for i in range(1, num_tables + 1)]
        self.queue = Queue()
        self.lock = Lock()
        self.customer_count = 0

    def customer_arrival(self,):
        while True:
            sleep(random.uniform(0.5, 2))
            with self.lock:
                self.customer_count += 1
                customer = Customer(self.customer_count)
            print(f'Посетитель {customer.number} прибыл.')
            self.queue.put(customer)

    def serve_customer(self, table):
        while True:
            if not table.is_busy and not self.queue.empty():
                customer = self.queue.get()
                table.is_busy = True
                print(f'Посетитель {customer.number} сел за стол {table.number}')
                sleep(random.uniform(2, 5))
                table.is_busy = False
                print(f'Посетитель {customer.number} покушал и ушёл со стола {table.number}.')
            else:
                sleep(1)

    def serve_at_table(self, table):
        while True:
            if not table.is_busy and not self.queue.empty():
                customer = self.queue.get()
                table.is_busy = True
                print(f'Посетитель {customer.number} сел за стол {table.number}')
                sleep(random.uniform(2, 5))  # Имитация времени обслуживания
                table.is_busy = False
                print(f'Посетитель {customer.number} покушал и ушёл со стола {table.number}.')
            else:
                sleep(0.1)


def main():
    cafe = Cafe(3)

    arrival_thread = Thread(target=cafe.customer_arrival)
    table_threads = [Thread(target=cafe.serve_at_table, args=(table,)) for table in cafe.tables]

    arrival_thread.start()
    for thread in table_threads:
        thread.start()
    arrival_thread.join()
    for thread in table_threads:
        thread.join()


if __name__ == "__main__":
    main()
