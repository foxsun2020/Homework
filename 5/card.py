"""
Function: Create series of cards and deliver to 3 participates.
Coding: utf-8
Author: Sun Yuexin
Date: 2020/11/12
"""
import random


def cards():
    pokers = []
    number = list(range(2, 11)) + ["A", "J", "Q", "K"]
    color = ['♥', '♠', '♦', '♣']
    for i in color:
        for j in number:
            pokers.append([i, j])
    pokers += ["Joker", "Joker"]
    return pokers


def deal(poker):
    li = {}
    people = ["player1", "player2", "player3"]
    for k in people:
        exact = random.sample(poker, 17)
        li.setdefault(k, exact)
        print(k, ">>>", li[k])
        for s in exact:
            poker.remove(s)
    print("Hole >>>>>>", poker)


if __name__ == '__main__':
    deal(cards())

