import readwordlist
import P1Search

wordlist = readwordlist.wordlist("words.txt")

frstlet = input("First Letter... ")
Seclet = input("Second Letter... ")
Thrlet = input("Third Letter... ")

P1Search.p1search(wordlist,frstlet,Seclet,Thrlet)



input("")
