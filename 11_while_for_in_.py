i = 1

while i < 5:
    i += 1
    print(i, end='')

for i in 'hello world':
    if i == ' ':
        continue
    print(i, end='')
    if i == 'd':
        break
else:
    print('break')

for i in range(5):
    print(i * 2, end='')
else:
    print('!')

# output: 2345helloworld02468!
