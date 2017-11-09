#!/usr/bin/env python
# -*- coding: utf-8 -*-

oneBase = 0x1DB
oneDelta = 1
heroBase = 0x45BF
heroDelta = 152
kingBase = 0x25454
kingDelta = 72
armyBase = 0x2618C
armyDelta = 8
cityBase = 0x26304
cityDelta = 81
horseBase = 0x23E45
horseDelta = 57

def addKing(bs, kingdoms):
    for i in range(len(kingdoms)):
        kingdom = kingdoms[i]
        bs[oneBase + oneDelta * kingdom.capital] = i
        bs[heroBase + heroDelta * kingdom.king] = i
        bs[heroBase + heroDelta * kingdom.king + 1] = kingdom.capital
        bs[heroBase + heroDelta * kingdom.king + 2] = 0x00
        bs[heroBase + heroDelta * kingdom.king + 3] = kingdom.capital
        bs[heroBase + heroDelta * kingdom.king + 4] = 0x00
        bs[heroBase + heroDelta * kingdom.king + 5] = 0x00
        bs[kingBase + kingDelta * i] = kingdom.king % 0x100
        bs[kingBase + kingDelta * i + 1] = int(kingdom.king / 0x100)
        bs[kingBase + kingDelta * i + 53] = i
        bs[armyBase + armyDelta * i] = i
        bs[armyBase + armyDelta * i + 2] = kingdom.king % 0x100
        bs[armyBase + armyDelta * i + 3] = int(kingdom.king / 0x100)
        bs[cityBase + cityDelta * kingdom.capital] = i
        bs[horseBase + horseDelta * i] = kingdom.king % 0x100
        bs[horseBase + horseDelta * i + 1] = int(kingdom.king /0x100)

def addHero(bs, kingdoms):
    for i in range(len(kingdoms)):
        kingdom = kingdoms[i]
        heros = kingdom.heroList
        for hero in heros:
            bs[heroBase + heroDelta * hero] = i
            bs[heroBase + heroDelta * hero + 1] = kingdom.capital
            bs[heroBase + heroDelta * hero + 2] = 0x00
            bs[heroBase + heroDelta * hero + 3] = kingdom.capital
            bs[heroBase + heroDelta * hero + 4] = 0x00
            bs[heroBase + heroDelta * hero + 5] = 0x03

def clearCity(bs, kingdoms):
    owns = list(map(lambda x: x.capital, kingdoms))
    for i in range(42):
        if i not in owns:
            for j in range(53):
                bs[cityBase + cityDelta * i + 5 + j] = 0x00

def genScen(kingdoms):
    f = open('ScenModel_B.s11', 'rb')
    bs = list(f.read())
    f.close()
    addKing(bs, kingdoms)
    addHero(bs, kingdoms)
    clearCity(bs, kingdoms)
    f = open('ScenTest.s11', 'wb')
    f.write(bytes(bs))
    f.close()

