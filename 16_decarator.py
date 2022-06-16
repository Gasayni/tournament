from time import time
from time import sleep as ts


def timer(func):
    """Декоратор. Выводит время работы задекорированной функции и возвращает ее результат"""

    def wrapped(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('Время работы функции {} секунд(ы)'.format(round(time() - start, 4)))
        return result
    return wrapped


def sleep(_func=None, *, sec=1):
    def slp(func):
        """Декоратор, который делает паузу перед выполнением n секунд"""

        def wrapped_func(*args, **kwargs):
            ts(sec)
            return func(*args, **kwargs)
        return wrapped_func

    if _func is None:
        return slp
    return slp(_func)


@timer
@sleep(sec=10)
def function():
    res = 0
    for _ in range(100 + 1):
        res += sum([i_num*2 for i_num in range(10000)])
    return res


print(function())
