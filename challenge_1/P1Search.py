#this module prints the first word in the list which contains the input letters in order


def p1search(wordlist,frstlet,Seclet,Thrlet):
    for x in wordlist:
        if frstlet in x:
            #if Seclet in x:
                #if Thrlet in x:
                    if x.find(frstlet)<x.find(Seclet)<x.find(Thrlet):
                        print("The word\n"+x+"\ncontains the letters\n"+frstlet+" "+Seclet+" and "+Thrlet+ " in that order.")
                        break
