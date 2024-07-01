import sys
from itertools import repeat


class EvenNumbers:

    def __init__(self, x, y):
        self.i = 0
        self.start = x if x % 2 == 0 else x + 1
        self.end = y
        self.current = self.start - 2

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.end:
            raise StopIteration()
        return self.current


en = EvenNumbers(10, 25)
print(en)
for i in en:
    print(i)
