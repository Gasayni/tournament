from random import randint


def summarize(a, b):
    return a + b


def multiply(a, b=3):
    return a * b


def do_nothing():
    pass


print(summarize(1, 14))  # output: 15
print(summarize('a', "b"))  # output: ab
print(multiply(2, 7))  # output: 14
print(multiply(2))  # output: 6
print(multiply("spam"))  # output: spamspamspam
print(do_nothing())  # output: None


def modify_list(lst, fun):
    for i, v in enumerate(lst):
        lst[i] = fun(v)


my_lst = [randint(1, 5) for x in range(3)]
modify_list(my_lst, multiply)
print(my_lst)
