my_dict = dict()
print(my_dict)  # output: {}

my_dict = {'dict': 1, 'dictionary': 2}
print(my_dict)  # output: {'dict': 1, 'dictionary': 2}

my_dict = dict(short='dict', long='dictionary')
print(my_dict)  # output: {'short': 'dict', 'long': 'dictionary'}

my_dict = dict([(1, 1), (2, 4)])
print(my_dict)  # output: {1: 1, 2: 4}

my_dict = dict.fromkeys(['a', 'b'])
print(my_dict)  # output: {'a': None, 'b': None}

my_dict = dict.fromkeys([(1, 1), 'b'], 100)
print(my_dict)  # output: {(1, 1): 100, 'b': 100}

my_dict = {'^'.join([str(a), str(b)]): a ** b for a in range(3, 6) for b in range(2, 4)}
print(my_dict)  # output: {'3^2': 9, '3^3': 27, '4^2': 16, '4^3': 64, '5^2': 25, '5^3': 125}
