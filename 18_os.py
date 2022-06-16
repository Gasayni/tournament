import os
from datetime import datetime as dt

path = os.path.abspath(__file__)
print(path)
print(path.split(os.path.sep))

dir_lst = os.listdir()
for i_elem in dir_lst:
    if os.path.isdir(i_elem):
        i_type = 'dir'
    elif os.path.islink(i_elem):
        i_type = 'link'
    elif os.path.isfile(i_elem):
        i_type = 'file'
    else:
        i_type = ''
    print('{type: <5} {size: >10} {time} {path}'.format(
        type=i_type,
        size=os.path.getsize(i_elem),
        time=dt.fromtimestamp(os.path.getctime(i_elem)).strftime('%b %d %Y'),
        path=os.path.abspath(i_elem)))
