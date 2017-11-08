#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl
from openpyxl import *
from langconv import *
from conf import *
from kingdom import *
import sys

class Hero(object):
    def __init__(self, hid, name, ability):
        self.hid = hid
        self.name = name
        self.ability = ability
    def __str__(self):
        return str(self.mid) + ' ' + self.name + ' ' + self.ability
    def __repr__(self):
        return self.__str__()

def readHero(wb):
    heroDic = {}
    ws = wb.get_sheet_by_name('全武将')
    for i in range(2,672):
        hid = int(ws['A'+str(i)].value)
        name = ws['B'+str(i)].value
        ability = ws['O'+str(i)].value
        heroDic[int(ws['A'+str(i)].value)] = Hero(hid, name, ability)
    return heroDic

def findByName(name, heroDic):
    ret = -1
    cname = Converter('zh-hant').convert(name)
    for _, hero in heroDic.items():
        if name == hero.name:
            ret = hero.hid
        elif name in special:
            ret = special[name]
        else:
            targetname = Converter('zh-hant').convert(hero.name)
            if cname == targetname:
                ret = hero.hid
        if ret != -1:
            break
    if ret == -1:
        print(name, ' give the id:')
        ret = int(input('>'))
    return ret
        
def findHerosID(playerID, heroNum, wb, kingID, heroDic):
    ws = wb.get_sheet_by_name('source')
    heroList = []
    for i in range(3, heroNum+3):
        heroID = findByName(ws.cell(row = i, column = playerID).value, heroDic)
        if heroID != kingID:
            heroList.append(heroID)
    heroList.sort()
    return heroList

def findCityID(cityName):
    ret = -1
    for cid, c in city.items():
        if cityName == c:
            ret = cid
            break
    if ret == -1:
        print(cityName, ' give the id:')
        ret = int(input('>'))
    return ret

def parseKingdom(playerNum, heroNum, wb):
    ws = wb.get_sheet_by_name('source')
    heroDic = readHero(wb)
    kingdoms = []
    citys = []
    for i in range(1, playerNum+1):
        kingID = findByName(ws.cell(row = 1, column = i).value, heroDic)
        cid = findCityID(ws.cell(row = 2, column = i).value)
        citys.append(cid)
        kingdom = Kingdom(kingID,  cid, findHerosID(i, heroNum, wb, kingID, heroDic))
        kingdoms.append(kingdom)
    return kingdoms

def main(playerNum, heroNum, inFile):
    wb = load_workbook(inFile)
    kingdoms = parseKingdom(playerNum, heroNum, wb)
    f = open('output.txt', 'w')
    for k in kingdoms:
        f.write(str(k))
        f.write('\n')
    f.close()
 
if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])

