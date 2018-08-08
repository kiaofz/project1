#this module outputs the variables longest(the longest word in the list) and highest(the length of the longest word)
from GetPath import wordlist

highest = 0
longest = ""
for x in wordlist:
    curlen = len(x)
    if curlen >= highest:
        longest = x
        highest = curlen
