# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card', 'f']

# %% ../nbs/00_card.ipynb 2
suits = ["♣️", "♦️", "♥️", "♠️"]

# %% ../nbs/00_card.ipynb 4
ranks = [None, "A"] + [str(x) for x in range(2, 11)] + ["J", "Q", "K"]

# %% ../nbs/00_card.ipynb 8
class Card:
    "A playing card"
    def __init__(self, 
                 suite: int, # An index into `suits`
                 rank: int): # An index into `ranks`
        self.suite,self.rank = suite,rank
    def __str__(self): return f"{ranks[self.rank]}{suits[self.suite]}"
    __repr__ = __str__
    
    def __eq__(self, other):
        return self.suite == other.suite and self.rank == other.rank

# %% ../nbs/00_card.ipynb 16
from fastcore.test import *
from fastcore.utils import *

# %% ../nbs/00_card.ipynb 18
test_eq(Card(suite=1, rank=3), Card(suite=1, rank=3))
test_ne(Card(suite=1, rank=3), Card(suite=1, rank=4))

# %% ../nbs/00_card.ipynb 19
@patch
def __eq__(self:Card, a:Card): return (self.suite,self.rank) == (a.suite,a.rank)

# %% ../nbs/00_card.ipynb 20
@patch
def __lt__(self:Card, a:Card): return (self.suite,self.rank) < (a.suite,a.rank)

# %% ../nbs/00_card.ipynb 21
assert Card(1, 3) < Card(2, 3)

# %% ../nbs/00_card.ipynb 23
def f(a, b):
    print (a, b)
