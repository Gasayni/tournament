file_in = open('zen.txt', 'r')
file_out = open('out.txt', 'w')

for line in file_in:
    file_out.write(line + "\n")

file_in.close()
file_out.close()


with open('zen.txt') as file:
    for i, line in enumerate(file):
        print(f"{i+1}.\t{line.strip()}")
