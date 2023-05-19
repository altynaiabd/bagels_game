import random, easygui

NUM_DIGITS = 3
MAX_GUESSES = 15


def main():
    easygui.msgbox('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a 3-digit number. Try to guess what it is.

Here are some clues:

When I say:

That means:

Pico      One digit is correct but in the wrong position.
Fermi     One digit is correct and in the right position.
Bagels    No digit is correct.''')

    while True:
        secretNum = getSecretNum()
        easygui.msgbox('I have thought up a number.')
        easygui.msgbox('You have {} guesses to get it'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(str(guess)) != NUM_DIGITS or not str(guess).isdecimal():
                guess = easygui.integerbox('Guess #{}: '.format(numGuesses), upperbound=999)
                if not guess:
                    break

            clues = getClues(guess, secretNum)
            easygui.msgbox(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                easygui.msgbox('You ran out of guesses.')
                easygui.msgbox('The answer was {}.'.format(secretNum))

        response = easygui.ynbox('Do you want to play again?')
        if not response:
            break
    easygui.msgbox('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    guess = str(guess)
    secretNum = str(secretNum)

    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(str(guess))):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()

