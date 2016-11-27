#
# Lizzie's homework program
#
# Who wants to be a mathionaire game.
#
# Rules of the game:
# 1. There are fifteen questions. These should become more difficult
# as the questions continue.
# 2. As long as the question is correct you move onto the next
# question. If you get the question wrong then the user gets one more go.
#

# Import the random number generating library so that numbers can be
# generated as required.
import random
# import os specific stuff to clear the terminal between questions
import os

# Set the variables to use in the game. Variable names should indicate
# what the variable does as much as possible.

noOfCorrectAnswers = 0
noOfWrongAnswers = 0
testingMode = 0                 # set to 1 to show answers, set to
                                # zero for production.
# Introduction text. It explains what is going to happen during the
# game. It then asks that the user hits the enter key to continue.
os.system('cls' if os.name == 'nt' else 'clear')
print "Welcome to who wants to be a millionaire."
print "\nYou will be asked to do sums using random numbers. There are"
print "additions, subtractions, multiplications and divisions"
print "The sums will get harder as the game progresses"
print "Good luck."

raw_input ("Press the return key to continue...")

# This is the main loop of the program. It will run while the number
# of correct answers is less than 14 and the number of incorrect
# answers is zero.
while noOfCorrectAnswers <= 14 and noOfWrongAnswers == 0:
        os.system('cls' if os.name == 'nt' else 'clear') # clear screen.

        # Create the two numbers to use in the sums. The numbers are in a range from 1 to 10 * question number.
        firstNumber = random.randint(((noOfCorrectAnswers+1)),((noOfCorrectAnswers+1)*8)) # Generate first number
        secondNumber = random.randint(((noOfCorrectAnswers+1)),((noOfCorrectAnswers+1)*8)) # Generate second number

        # Because subtraction of a bigger number from a smaller number
        # is a little tricky run comparison of firstNumber and
        # secondNumber and switch them around it second number is bigger.
        if firstNumber < secondNumber and noOfCorrectAnswers >= 4 and noOfCorrectAnswers < 8:
                tmpNumber = firstNumber
                firstNumber = secondNumber
                secondNumber = tmpNumber

        # Want to make division use large enough numbers to be a
        # challenge, but not have decimal places when dividing.
        # Reverse engineer the 'big' number by creating result and
        # divisor and then multiplying them together.
        if noOfCorrectAnswers >= 12:
                secondNumber = random.randint(1,12)
                multiplier = random.randint(1,12)
                firstNumber = secondNumber * multiplier

        # Present the question to the user.
        #
        # In Python it is normal to count from zero. Therefore the 15
        # questions run from 0-14. Ask 4 addition, 4 subtraction, four
        # multiplicatio and three division. The following if..elif
        # flow control checks which number question is being asked and
        # applies the appropriate question type. The print statement
        # then displays the question with appropriate text *and*
        # calculates the answer that the user will need to enter.
        if noOfCorrectAnswers < 4:
                print "Question %s: Tell me the answer to %s plus %s, type your answer below" % ((noOfCorrectAnswers+1),firstNumber, secondNumber)
                answer = firstNumber + secondNumber
        elif noOfCorrectAnswers >= 4 and noOfCorrectAnswers < 8:
                print "Question %s: Tell me the answer to %s minus %s, type your answer below" % ((noOfCorrectAnswers+1),firstNumber, secondNumber)
                answer = firstNumber - secondNumber
        elif noOfCorrectAnswers >=8 and noOfCorrectAnswers < 12:
                print "Question %s: Tell me the answer to %s times %s, type your answer below" % ((noOfCorrectAnswers+1),firstNumber, secondNumber)
                answer = firstNumber * secondNumber
        elif noOfCorrectAnswers >=12:
                print "Question %s: Tell me the answer to %s divided by %s, type your answer below" % ((noOfCorrectAnswers+1),firstNumber, secondNumber)
                answer = firstNumber / secondNumber

        # I introduced a testing mode (variable set at the head of the
        # file). If testingMode is 1 then the answer is displayed
        # after the question. Saves you having to calculate the
        # answers while testing the program. Make sure testingMode is
        # set to zero for 'production'.
        if testingMode == 1:
                print "During Testing the Answer is: %s" % answer
        else:
                print "\n"
        # request the answer and compare it to the answer as
        # calculated by the program. If they match increase the number
        # of correct answers by 1. Write the sum to the text file, and
        # display the amount won having got the question correct.
        guess = input("Tell me your answer: ")
        if guess == answer:
                print "Well done, the answer is %s" % guess
                noOfCorrectAnswers = noOfCorrectAnswers + 1
                if noOfCorrectAnswers == 1:
                        print "\nYou have made 100"
                elif noOfCorrectAnswers ==2:
                        print "\nYou have made 200"
                elif noOfCorrectAnswers == 3:
                        print "\nYou have made 300"
                elif noOfCorrectAnswers == 4:
                        print "\nYou have made 500"
                elif noOfCorrectAnswers == 5:
                        print "\nYou have made 1000"
                elif noOfCorrectAnswers == 6:
                        print "\nYou have made 2000"
                elif noOfCorrectAnswers == 7:
                        print "\nYou have made 4000"
                elif noOfCorrectAnswers == 8:
                        print "\nYou have made 8000"
                elif noOfCorrectAnswers == 9:
                        print "\nYou have made 16000"
                elif noOfCorrectAnswers == 10:
                        print "\nYou have made 32000"
                elif noOfCorrectAnswers == 11:
                        print "\nYou have made 64000"
                elif noOfCorrectAnswers == 12:
                        print "\nYou have made 125000"
                elif noOfCorrectAnswers ==13:
                        print "\nYou have made 250000"
                elif noOfCorrectAnswers == 14:
                        print "\nYou have made 500000"
                raw_input("Press enter to continue")
        # If the answer is wrong then the user gets another go. If the
        # second go is correct then the game continues. If it is wrong
        # the game ends. The code here is really scrappy and could do
        # with a major re-write. It was the last thing I added, and it
        # was only added as Lizzie wanted to get a second chance. The
        # logic is incomplete. Sorry!
        else:
                noOfWrongAnswers = noOfWrongAnswers + 1
                # print "Sorry, that was wrong. The answer was %s" %
                # answer
                secondChance = 0
                print "That was the wrong answer. Try again"
                retry = input("have another go: ")
                if retry != answer and secondChance < 3:
                        secondChance = secondChance + 1
                else:
                        noOfWrongAnswers = 0
                        noOfCorrectAnswers = noOfCorrectAnswers + 1
                if noOfCorrectAnswers == 1:
                        print "\nYou have made 100"
                elif noOfCorrectAnswers ==2:
                        print "\nYou have made 200"
                elif noOfCorrectAnswers == 3:
                        print "\nYou have made 300"
                elif noOfCorrectAnswers == 4:
                        print "\nYou have made 500"
                elif noOfCorrectAnswers == 5:
                        print "\nYou have made 1000"
                elif noOfCorrectAnswers == 6:
                        print "\nYou have made 2000"
                elif noOfCorrectAnswers == 7:
                        print "\nYou have made 4000"
                elif noOfCorrectAnswers == 8:
                        print "\nYou have made 8000"
                elif noOfCorrectAnswers == 9:
                        print "\nYou have made 16000"
                elif noOfCorrectAnswers == 10:
                        print "\nYou have made 32000"
                elif noOfCorrectAnswers == 11:
                        print "\nYou have made 64000"
                elif noOfCorrectAnswers == 12:
                        print "\nYou have made 125000"
                elif noOfCorrectAnswers ==13:
                        print "\nYou have made 250000"
                elif noOfCorrectAnswers == 14:
                        print "\nYou have made 500000"
                # raw_input("Press enter to continue")

# Ending the game (if 15 correct answers you're a millionaire.
# If you haven't got all 15 right then display how many were correct.

if noOfCorrectAnswers == 15:
        print "\nCongratulations, You're a millionaire"
else:
        print "\nYou got %s questions right" % noOfCorrectAnswers
