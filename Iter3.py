class PowerOfThreeIterator:
    def __init__(self, max_degree=10):
        self.current = 0
        self.max_degree = max_degree

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_degree:
            raise StopIteration
        val = 3 ** self.current
        self.current += 1
        return val

for number in PowerOfThreeIterator(5):
    print(number)