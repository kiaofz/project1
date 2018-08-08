#this module outputs the variables readme, a string version of the textfile, and wordlist
import os

def wordlist(file_name):
    contentstring = open(file_name).read()
    return contentstring.split('\n')





#readme = open(r'C:\Users\dave\search_project\project1\challenge_1\words.txt').read()
