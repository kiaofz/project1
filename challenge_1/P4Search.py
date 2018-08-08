#This module outputs a the dictionary lenfreq containing the lengths of words and respective frequencies
from GetPath import wordlist
from P3Search import highest


lendict = {}     #this is a dictionary of the words in worlist and their lengths
for x in wordlist:
    lendict[x] = len(x)

lenfreq = {}      #this is a dict of frequencies of certain word lengths
highest +=1
for y in range(1,highest):
    for z in lendict:
        if lendict[z] == y:
            if y in lenfreq:
                lenfreq[y] += 1
            else:
                lenfreq[y] = 1
