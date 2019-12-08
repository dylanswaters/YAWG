# Starts always grabs one

starts = [
"Ald",
"Ver",
"Gerr",
"Dosh",
"Brorst",
"Jval",
"Mort",
"Nev",
"Goods",
"Barv",
"Orst",
"Torv",
"Ost",
"Medd",
"Ar",
"De",
"Drisk",
"Dans",
"Zvech",
"Hans",
"Ur",
"An",
"Gretch",
"Thraine"
]

# Mids 80% chance picking
mids = [
"un",
"at",
"ock",
"ish",
"born",
"desh",
"rot",
"svalt",
"good",
"grad",
"vern",
"land",
"dar",
"vos",
"en",
"ol",
"gu",
"tell",
"dan",
"vins",
"ok",
"rav",
"o"
]

# Ends 30% chance picking
ends = [
"ia",
"er",
"at",
"on",
"gong",
"tov",
"lund"
]

# Revolution titles, where ? is replaced with previous name
revNames = [
"New ?",
"?\'s People\'s Republic",
"Greater ?",
"United ? Republic",
"Revolutionary ?",
"People\'s ?",
"Free ?",
"United Union\'s of ?",
"Communes of ?",
"Glorious ?",
"Worker\'s ?",
"Independent ?",
"Provisional ?",
"? Rebellion",
"?",
]

import random

def getName():
    retName = ""
    retName += starts[random.randint(0,len(starts)-1)]
    if(random.randint(0,100) < 80):
        retName += mids[random.randint(0,len(mids)-1)]
    if(random.randint(0,100) < 30):
        retName += ends[random.randint(0,len(ends)-1)]
    return retName

def getRevName(name):
    revName = revNames[random.randint(0,len(revNames)-1)]
    retName = revName.replace("?", name)
    return retName
