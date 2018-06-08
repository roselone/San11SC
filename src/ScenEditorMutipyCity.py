#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

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

def createKingdom(bs, kingdom, i):
    bs[oneBase + oneDelta * kingdom.capital[0]] = i
    bs[heroBase + heroDelta * kingdom.king] = i
    bs[heroBase + heroDelta * kingdom.king + 1] = kingdom.capital[0]
    bs[heroBase + heroDelta * kingdom.king + 2] = 0x00
    bs[heroBase + heroDelta * kingdom.king + 3] = kingdom.capital[0]
    bs[heroBase + heroDelta * kingdom.king + 4] = 0x00
    bs[heroBase + heroDelta * kingdom.king + 5] = 0x00
    bs[kingBase + kingDelta * i] = kingdom.king % 0x100
    bs[kingBase + kingDelta * i + 1] = int(kingdom.king / 0x100)
    bs[kingBase + kingDelta * i + 53] = i
    bs[armyBase + armyDelta * i] = i
    bs[armyBase + armyDelta * i + 2] = kingdom.king % 0x100
    bs[armyBase + armyDelta * i + 3] = int(kingdom.king / 0x100)
    for city in kingdom.capital:
        bs[cityBase + cityDelta * city] = i
    bs[horseBase + horseDelta * i] = kingdom.king % 0x100
    bs[horseBase + horseDelta * i + 1] = int(kingdom.king /0x100)

    heros = kingdom.heroList
    for hero in heros:
        city = random.sample(kingdom.capital, 1)[0]
        bs[heroBase + heroDelta * hero] = i
        bs[heroBase + heroDelta * hero + 1] = city
        bs[heroBase + heroDelta * hero + 2] = 0x00
        bs[heroBase + heroDelta * hero + 3] = city
        bs[heroBase + heroDelta * hero + 4] = 0x00
        bs[heroBase + heroDelta * hero + 5] = 0x03

def genScen(kingdoms):
    f = open('ScenModel_D.s11', 'rb')
    bs = list(f.read())
    f.close()
    for i in list(range(len(kingdoms))):
        kingdom = kingdoms[i]
        createKingdom(bs, kingdom, i)
    f = open('ScenTest.s11', 'wb')
    f.write(bytes(bs))
    f.close()

