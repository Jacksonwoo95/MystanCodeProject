"""
File: hangman.py
Name:吳禹
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    in while loop , input guess, calculate life
    make a function , do string manipulation
    """
    ans = random_word()
    life = int(N_TURNS)
    my_ans = ""  # first string
    for i in range(len(ans)):
        my_ans += "-"

    while True:
        if life == 0:
            print("You are completely hung:(")
            print("The answer is: " + ans)
            break
        print("The word looks like: " + my_ans)
        print("You have " + str(life) + " wrong guesses left.")
        input_ch = input("Your guess: ")
        input_ch = input_ch.upper()

        while input_ch.isdigit() or len(input_ch) > 1:
            print("Illegal format.")
            input_ch = input("Your guess: ")
        if input_ch not in ans:
            life -= 1
        my_ans = hangman(ans, input_ch, my_ans)

        if my_ans == ans:
            print("You win!!")
            print("The answer is: " + ans)
            break


def hangman(ans, input_ch, my_ans):
    """
    :param ans: string,random
    :param input_ch: string, a letter
    :param my_ans: string, if ch in ans, do string manipulate
    :return: string
    """
    new_ans = ""
    for i in range(len(ans)):
        ch = ans[i]
        ch_my_ans = my_ans[i]
        if ch_my_ans.isalpha():
            new_ans += ch_my_ans
        elif input_ch == ch:
            new_ans += input_ch
        else:
            new_ans += "-"
    if input_ch in ans:
        print("You are correct!")
    else:
        print("There is no " + input_ch + "'s in the word.")

    return new_ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
