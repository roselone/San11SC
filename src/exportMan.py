#!/usr/bin/env python
# coding:utf8

import openpyxl
from openpyxl import *
from langconv import *
import sys

class Man(object):
    def __init__(self, mid, name, ability):
        self.mid = mid
        self.name = name
        self.ability = ability
    def __str__(self):
        return str(self.mid) + ' ' + self.name + ' ' + self.ability
    def __repr__(self):
        return self.__str__()

def readMan():
    manDic = {}
    wb = load_workbook('20171017.xlsx')
    ws = wb.get_sheet_by_name('全武将'.decode('utf-8'))
    for i in range(2,672):
        mid = int(ws['A'+str(i)].value)
        name = ws['B'+str(i)].value
        ability = ws['O'+str(i)].value
        manDic[int(ws['A'+str(i)].value)] = Man(mid, name, ability)
    return manDic

def findByName(name, manDic):
    ret = -1
    for _, man in manDic.items():
        if name == man.name:
            ret = man.mid
            break
    if ret == -1:
        cname = Converter('zh-hant').convert(name)
        for _, man in manDic.items():
            targetname = Converter('zh-hant').convert(man.name)
            if cname == targetname:
                ret = man.mid
                break
    if ret == -1:
        print name, " give the id:"
        ret = int(raw_input(">"))
    return ret
        
def findMID(playerNum, manNum):
    wb = load_workbook('20171101.xlsx')
    ws = wb.get_sheet_by_name('source')
    manDic = readMan()
    ret = []
    for i in range(1, playerNum+1):
        manList = []
        for j in range(1, manNum+1):
            manList.append(findByName(ws.cell(row = j, column = i).value, manDic))
        manList.sort()
        ret.append(manList)
    return ret

def main(playerNum, manNum):
    ret = findMID(playerNum, manNum)
    f = open('output.txt', 'w')
    for i in ret:
        i = map(lambda x: str(x), i)
        f.write(' '.join(i))
        f.write('\n')
    f.close()
 
if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))

