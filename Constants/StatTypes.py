
class StatTypes:
    def __init__(self):
        self.MAXHPSTAT = 0
        self.HPSTAT = 1
        self.SIZESTAT = 2
        self.MAXMPSTAT = 3
        self.MPSTAT = 4
        self.NEXTLEVELEXPSTAT = 5
        self.EXPSTAT = 6
        self.LEVELSTAT = 7
        self.INVENTORY0STAT = 8
        self.INVENTORY1STAT = 9
        self.INVENTORY2STAT = 10
        self.INVENTORY3STAT = 11
        self.INVENTORY4STAT = 12
        self.INVENTORY5STAT = 13
        self.INVENTORY6STAT = 14
        self.INVENTORY7STAT = 15
        self.INVENTORY8STAT = 16
        self.INVENTORY9STAT = 17
        self.INVENTORY10STAT = 18
        self.INVENTORY11STAT = 19
        self.ATTACKSTAT = 20
        self.DEFENSESTAT = 21
        self.SPEEDSTAT = 22
        self.VITALITYSTAT = 26
        self.WISDOMSTAT = 27
        self.DEXTERITYSTAT = 28
        self.CONDITIONSTAT = 29
        self.NUMSTARSSTAT = 30
        self.NAMESTAT = 31
        self.TEX1STAT = 32
        self.TEX2STAT = 33
        self.MERCHANDISETYPESTAT = 34
        self.CREDITSSTAT = 35
        self.MERCHANDISEPRICESTAT = 36
        self.ACTIVESTAT = 37
        self.ACCOUNTIDSTAT = 38
        self.FAMESTAT = 39
        self.MERCHANDISECURRENCYSTAT = 40
        self.CONNECTSTAT = 41
        self.MERCHANDISECOUNTSTAT = 42
        self.MERCHANDISEMINSLEFTSTAT = 43
        self.MERCHANDISEDISCOUNTSTAT = 44
        self.MERCHANDISERANKREQSTAT = 45
        self.MAXHPBOOSTSTAT = 46
        self.MAXMPBOOSTSTAT = 47
        self.ATTACKBOOSTSTAT = 48
        self.DEFENSEBOOSTSTAT = 49
        self.SPEEDBOOSTSTAT = 50
        self.VITALITYBOOSTSTAT = 51
        self.WISDOMBOOSTSTAT = 52
        self.DEXTERITYBOOSTSTAT = 53
        self.OWNERACCOUNTIDSTAT = 54
        self.RANKREQUIREDSTAT = 55
        self.NAMECHOSENSTAT = 56
        self.CURRFAMESTAT = 57
        self.NEXTCLASSQUESTFAMESTAT = 58
        self.LEGENDARYRANKSTAT = 59
        self.SINKLEVELSTAT = 60
        self.ALTTEXTURESTAT = 61
        self.GUILDNAMESTAT = 62
        self.GUILDRANKSTAT = 63
        self.BREATHSTAT = 64
        self.XPBOOSTEDSTAT = 65
        self.XPTIMERSTAT = 66
        self.LDTIMERSTAT = 67
        self.LTTIMERSTAT = 68
        self.HEALTHPOTIONSTACKSTAT = 69
        self.MAGICPOTIONSTACKSTAT = 70
        self.BACKPACK0STAT = 71
        self.BACKPACK1STAT = 72
        self.BACKPACK2STAT = 73
        self.BACKPACK3STAT = 74
        self.BACKPACK4STAT = 75
        self.BACKPACK5STAT = 76
        self.BACKPACK6STAT = 77
        self.BACKPACK7STAT = 78
        self.HASBACKPACKSTAT = 79
        self.TEXTURESTAT = 80
        self.PETINSTANCEIDSTAT = 81
        self.PETNAMESTAT = 82
        self.PETTYPESTAT = 83
        self.PETRARITYSTAT = 84
        self.PETMAXABILITYPOWERSTAT = 85
        self.PETFAMILYSTAT = 86
        self.PETFIRSTABILITYPOINTSTAT = 87
        self.PETSECONDABILITYPOINTSTAT = 88
        self.PETTHIRDABILITYPOINTSTAT = 89
        self.PETFIRSTABILITYPOWERSTAT = 90
        self.PETSECONDABILITYPOWERSTAT = 91
        self.PETTHIRDABILITYPOWERSTAT = 92
        self.PETFIRSTABILITYTYPESTAT = 93
        self.PETSECONDABILITYTYPESTAT = 94
        self.PETTHIRDABILITYTYPESTAT = 95
        self.NEWCONSTAT = 96
        self.FORTUNETOKENSTAT = 97
        self.SUPPORTERPOINTSSTAT = 98
        self.SUPPORTERSTAT = 99
        self.CHALLENGERSTARBGSTAT = 100
        self.PROJECTILESPEEDMULT = 102
        self.PROJECTILELIFEMULT = 103

    def nameOf(self, type):
        if type in self.dict.values():
            for key in self.dict.keys():
                if type == self.dict[key]:
                    return key
        return "UNKNOWNSTAT"
