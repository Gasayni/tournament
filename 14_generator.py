import math


def prime_number_generator(num):
    for n in range(1, num+1, 2):
        if n < 2:
            continue
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                break
        else:
            yield n


number = int(input("Enter a number: "))

for x in prime_number_generator(number):
    print(x)
