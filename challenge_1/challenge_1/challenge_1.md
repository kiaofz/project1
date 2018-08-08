# Challenge #1

The goal of this challenge is to start thinking in
abstractions—layering your code so that each layer builds on the one
below.

It might help to think of the problem in terms of words:

* I need to find a word that contains xxx.

This can become

* I need to:

  1. read the dictionary and 
  2. for each word
     2.1 check to see if a word matches the pattern xxx.
     
So now you're looking at at least two methods/functions, and some kind
of loop. 

Then, for each of the steps, break it down the same way. Continue
until you have something expressible as one or two lines of code.


## Problem 1

The file `words.txt` contains about 8900 words, one per line.

1. Write a program to find the first word that contains the letters
   "a", "b", and "c" in that order, potentially separated by other
   layers. (Hint: the answer is "abstract")
   
2. Write a program to find the first word that contains the letters
   "l", "m", and "n" in that order, potentially separated by other
   layers.
   
3. Write a program that takes three letters from the user and finds
   the first word that contains those three in order.
   

# Problem 2

4. Write a program to find the all the words that contains three sets of
   duplicated letters (there are 4 of them).

# Problem 3

5. Write a program that prints the longest word.

# Problem 4

6. Write a problem that prints a table showing the frequencies of word
   lengths:
   
       Word length      Count
         4                xxx
         5                yyy
         
         

