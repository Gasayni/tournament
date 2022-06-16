def factorial(n):
    if n > 0:
        if n == 1:
            return n
        return n * factorial(n-1)
    elif n == 0:
        return n
    return None


num = int(input("Enter a number: "))

print(factorial(num))
