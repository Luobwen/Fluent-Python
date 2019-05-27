# Python的魔术方法

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print(choice(deck))  # random包下的choice函数，实现从一个序列中随机抽取一个元素
print(deck[:3])
print(deck[12::13])

# 实现__getitem__后，该类就变为可迭代的了
for card in deck:
    print(card)

# 也可以使用in进行隐式迭代
print(Card('1', 'spades') in deck)

# 也可以实现排序


# ==============================================================================================

import math

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        return bool(abs(self))


v1 = Vector(2, 4)
v2 = Vector(6, 8)
print(v1 + v2)
print((v1 * 3))   # 不能写成3 * v1, ？？？
print(abs(v2))
print(bool(v1))