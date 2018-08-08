from GetPath import wordlist
from P2Input import sets,numsets

ABC = 'abcdefghijklmnopqrstuvwxyz'
for x in wordlist:
    letnum = 0
    for let in ABC:
        if x.count(let) >= numsets:
            letnum +=1
    if letnum >= sets:
        print(x)
