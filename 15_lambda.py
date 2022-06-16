from typing import List

strings: List[str] = ['d', 'e', 'c', 'b', 'a']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

new_lst = list(map(lambda x, y: (x, y), numbers, strings))
print(new_lst)

sort_key = lambda x: x[1]

for i_elem in sorted(new_lst, key=sort_key):
    print(i_elem)
