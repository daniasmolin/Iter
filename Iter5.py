def make_accumulator():
    total = 0
    def add(value):
        nonlocal total
        total += value
        return total
    return add

sum_generator = make_accumulator()

print(sum_generator(5))   # Виведе: 5
print(sum_generator(10))  # Виведе: 15
print(sum_generator(3))   # Виведе: 18