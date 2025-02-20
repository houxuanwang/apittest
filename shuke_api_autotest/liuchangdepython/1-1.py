import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FranceDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split( )

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


print(Card)
print(type(Card))
print(Card(1,1))
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()
a = FranceDeck
print("___________________________________________________")

print(a)
print(type(a))
print(id(a))
print("___________________________________________________")
b= FranceDeck()
print(b)
print(type(b))
print(id(b))
print("___________________________________________________")

c = FranceDeck
print(c)
print(type(c))
print(id(c))
d = FranceDeck()
print(d.suits)
print(d.ranks)
print(d._cards)
print(d.__len__())
print(d.__getitem__(0))
print(len(d))
print(d)
from random import choice
choice(d[:3])
for i in d:
    print(i)
print(FranceDeck())
print(Card(rank='A', suit='hearts') in d)
print(Card(rank='A', suit='hearts'))
print(type(Card(rank='A', suit='hearts')))

from pathlib import Path
file_path_root = Path(__file__).resolve().parent.parent
print(file_path_root)
print("1111111111111111111111111111111111111111111")
print(__file__)
print(__file__)
print(Path(__file__))
print(Path(__file__).resolve().parent)

a = "hello"
b = a.split('e')
print(b)

import subprocess

# 执行命令并等待其完成
result = subprocess.run(['ls', '-l'], capture_output=True, text=True,shell=True)

# 输出命令的返回码
print('Return Code:', result.returncode)

# 输出命令的标准输出
print('Standard Output:')
print(result.stdout)

# 输出命令的标准错误输出
print('Standard Error:')
print(result.stderr)