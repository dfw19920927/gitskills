'''
如何引用其他路径下的python文件
引用“D:/DFWworkspace/PY4E”中的first.py
'''

import sys

sys.path.append(r"D:/DFWworkspace/PY4E")

import first

a = first.add(3, 5, 8)
print(a)
