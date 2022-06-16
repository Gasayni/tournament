my_range = range(10)
print(my_range)  # output: range(0, 10)

my_list = [c * (c + 1) for c in range(10)]
print(my_list)  # output: [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

for i in my_range:
    print(i, end=' ')  # output: 0 1 2 3 4 5 6 7 8 9

print("\n")

for i in range(10, 0, -2):
    print(i, end=' ')  # output: 10 8 6 4 2
