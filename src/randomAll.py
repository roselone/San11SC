#!/usr/bin/env python
# -*- coding: utf-8 -*-

from openpyxl import *

from conf import *
from kingdom import *

import exportMan

import sys
import random
import codecs

from ScenEditor import *

def loadKeyHeros(inFile, heroDic):
    wb = load_workbook(inFile)
    ws = wb.get_sheet_by_name('sort')
    keyHeros = []
    for i in range(1, 217):
        heroID = exportMan.findByName(ws.cell(row = i, column = 1).value, heroDic)
        keyHeros.append(heroID)
    restHeros = []
    for heroID in heroDic.keys():
        if heroID not in keyHeros:
            restHeros.append(heroDic[heroID])
    return keyHeros, restHeros

def randCity(playerNum):
    for i in [0, 1, 18, 27, 40, 41]:
        city.pop(i)
    cities = random.sample(city.keys(), playerNum)
    return cities

def main(playerNum):
    heroDic = exportMan.readHero('hero.csv')
    keyHeros, restHeros = loadKeyHeros('heroSort.xlsx', heroDic)
    heroLists = []
    for i in list(range(playerNum)):
        heroLists.append([])
    roundKey = int(len(keyHeros) / playerNum)
    for heroID in keyHeros[playerNum * roundKey:]:
        restHeros.append(heroDic[heroID])
    for i in list(range(roundKey)):
        ran = random.sample(keyHeros[i*playerNum:(i+1)*playerNum], playerNum)
        for j in list(range(playerNum)):
            heroLists[j].append(ran[j])
    restHeros.sort(key = lambda x: x.baseEvaluate, reverse = True)
    roundKey = int(len(restHeros) / playerNum)
    for i in list(range(roundKey)):
        ran = random.sample(restHeros[i*playerNum:(i+1)*playerNum], playerNum)
        for j in list(range(playerNum)):
            heroLists[j].append(ran[j].hid)
    for i in restHeros[playerNum * roundKey:]:
        heroLists[random.randint(0, playerNum-1)].append(i.hid)

    kingdoms = []
    cities = randCity(playerNum)

    for i in list(range(playerNum)):
        kingdom = Kingdom(heroLists[i][0], cities[i], heroLists[i])
        kingdoms.append(kingdom)

    f = open('output.txt', 'w')
    for k in kingdoms:
        f.write(str(k))
        f.write('\n')
    f.close()
    genScen(kingdoms)

if __name__ == '__main__':
    default = 8
    if len(sys.argv) == 2 :
        default = int(sys.argv[1])
    main(default)
