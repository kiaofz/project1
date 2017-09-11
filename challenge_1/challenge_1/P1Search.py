#this module prints the first word in the list which contains the input letters in order
from GetPath import wordlist
from P1Input import frstlet
from P1Input import Seclet
from P1Input import Thrlet


for x in wordlist:
    if frstlet in x:
        if Seclet in x:
            if Thrlet in x:
                if x.find(frstlet)<x.find(Seclet)<x.find(Thrlet):
                    print("The word\n"+x+"\ncontains the letters\n"+frstlet+" "+Seclet+" and "+Thrlet+ " in that order.")
                    break
