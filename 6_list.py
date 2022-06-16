my_list = list('hello')
print(my_list)  # output: ['h', 'e', 'l', 'l', 'o']

empty_list = list()

my_list = ['h', 'e', ['llo'], 2]
print(my_list)  # output: ['h', 'e', ['llo'], 2]

my_list.append(empty_list)
print(my_list)  # output: ['h', 'e', ['llo'], 2, []]
print(my_list[3])  # output: 2

my_element = my_list.pop(3)
print(my_element)  # output: 2
print(my_list)  # output: ['h', 'e', ['llo'], []]

my_list = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
print(my_list)  # output: ['ls', 'lp', 'lm', 'ss', 'sp', 'sm', 'ts', 'tp', 'tm']
