def make_adder(fixed_value):
    def add(value):
        return fixed_value + value
    return add
add_five = make_adder(5)
print(add_five(10))  # Виведе: 15
print(add_five(3))   # Виведе: 8