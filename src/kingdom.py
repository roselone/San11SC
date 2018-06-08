#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Hero(object):
    def __init__(self, data):
        self.hid     = int(data[0])
        self.name    = data[1]
        self.defense = int(data[2])
        self.attack  = int(data[3])
        self.IQ      = int(data[4])
        self.EQ      = int(data[5])
        self.charm   = int(data[6])
        self.pikeman     = data[8]
        self.halberdier  = data[9]
        self.crossbowman = data[10]
        self.cavalryman  = data[11]
        self.weapon      = data[12]
        self.navy        = data[13]
        self.ability     = data[14]
        self.baseEvaluate = self.defense + self.attack + self.IQ
    def __str__(self):
        return str(self.hid) + ' ' + self.name + ' ' + self.ability
    def __repr__(self):
        return self.__str__()

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
