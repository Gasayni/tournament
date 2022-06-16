my_set = set()
print(my_set)  # output: set()

my_set = set('hello')
print(my_set)  # output: {'h', 'e', 'l', 'o'}

my_set = {i * i for i in range(10)}
print(my_set)  # output: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

my_set = {i / i for i in range(1, 10)}
print(my_set)  # output: {1.0}
