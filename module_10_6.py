from multiprocessing import Queue, Lock, Process


class WarehouseManager:
    def __init__(self):
        self.data = {}
        self.receipt = "receipt"
        self.shipment = "shipment"
        self.queue = Queue()
        self.lock = Lock()
        self.requests = [
            ("product1", "receipt", 100),
            ("product2", "receipt", 150),
            ("product1", "shipment", 30),
            ("product3", "receipt", 200),
            ("product2", "shipment", 50)
        ]

    def process_request(self):
        for product, action, amount in self.requests:
            with self.lock:
                if product not in self.data:
                    self.data[product] = 0
                if action == "receipt":
                    self.data[product] += amount
                elif action == "shipment":
                    self.data[product] = max(0, self.data[product] - amount)

    def run(self):
        self.process_request()
        q = Process(target=WarehouseManager)
        q.start()
        q.join()


if __name__ == '__main__':
    manager = WarehouseManager()
    manager.run()
    print(manager.data)
