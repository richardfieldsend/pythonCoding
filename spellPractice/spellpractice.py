#
# A simple program to enable practice of spellings for Lizzie.
#
# I'm writing this in Python cos that is what I am most comfortable with.
#
# Notes on the program ahead of actually coding it.
#
# I will store the correct spellings in a file called 'spellings.txt'.
#
# The file format for the file is one word per line. In the initial
# iteration I will  read the words from the file a line at a time and
# then test the spelling of that particular word. I will then keep a
# running total of number of words correct vs. number of words
# tested. This information will then be presented when the words run
# out.

# Import os library which is used to clear the screen.
import os
import sys
import fileinput

# In order to do the scoring: set values for number correct and number
# of questions and set both to zero. These will be incremented at
# appropriate places.
noRight = 0
noTested = 0

# Open the file 'spellings.txt' for reading
# spellings = open('spellings.txt','r')
filename = sys.argv[-1]
spellings = open(filename,'r')

# Introduce the program, and wait for a return key before starting.
os.system('cls' if os.name == 'nt' else 'clear')
print "Practice your spelling\n======== ==== ========\n"

# List the words that will be tested so that you can read through them
# before beginning.

# I want to loop through the file line by line
testword = spellings.readline()

while testword:
    testword = testword.rstrip()
    print testword
    testword = spellings.readline()

raw_input ("\n\nPress the return key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

spellings = open(filename,'r')
testword = spellings.readline()

# This is the main body of the program. The loop will iterate over the
# spelling file a line at a time.
while testword:
    # use .rstrip to remove the newline and white space at the end of
    # the test word.
    testword = testword.rstrip()

    # The question (numbered) is asked by presenting the word to be
    # spelled. The user is invited to
    print "Question %s: spell: %s\n" % ((noTested + 1), testword)
    raw_input ("Press the return key and then type the word...")
    os.system('cls' if os.name == 'nt' else 'clear')
    userSpell = raw_input("Type the word: ")
    noTested = noTested + 1
    if userSpell.lower() == testword.lower():
        print "Well done, you spelled the word correctly.\n"
        noRight = noRight + 1
    else:
        print "Sorry, the word is spelled %s.\n" % testword
    testword = spellings.readline()


spellings.close()

print "Thank you for playing. You got %s/%s right" % (noRight, noTested)
