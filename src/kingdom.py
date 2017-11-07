#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Kingdom(object):
    def __init__(self, king, capital, heroList):
        self.king = king
        self.capital = capital
        self.heroList = heroList

    def __str__(self):
        heros = map(lambda x: str(x), self.heroList)
        return str(self.king) + ' : ' + str(self.capital) + ' [' + ' '.join(heros) + ']'

    def __repr__(self):
        return self.__str__()
