#this module outputs the variables readme, a string version of the textfile, and wordlist
import os

file_name = 'words.txt'
cur_dir = os.getcwd()

path_answer=input("Please input document file file path. If 'n' is input, this program will search the current working directory for 'words.txt'")
if path_answer == 'n':
    file_list = os.listdir(cur_dir)
    if file_name in file_list:
        readme = open(cur_dir + r'\words.txt').read()
        wordlist = readme.split('\n')
    else:
        print("That file cannot be found.")

elif 'C' in path_answer:
    readme = open(path_answer).read()
    wordlist = readme.split('\n')

else:
    readme = open(cur_dir + r'\words.txt').read()
    wordlist = readme.split('\n')


#readme = open(r'C:\Users\dave\search_project\project1\challenge_1\words.txt').read()
