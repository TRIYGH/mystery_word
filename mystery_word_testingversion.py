#W1D4 Hangman   235,886

import time
import random


def word_difficulty(easy_words, normal_words, hard_words):
    entry = input("Select difficulty level: (E)asy, (N)ormal, (H)ard:  ").lower()
    if entry == 'e':
        return easy_words
    elif entry == 'n':
        return normal_words
    elif entry == 'h':
        return hard_words


def get_myst_word(game_list):
    x = len(game_list)
    y = random.randint(1,x)
    return game_list[y]


def display_board(guesses_left, letters_to_display,myst_word, mwl, all_guesses):
    print("\n"*50)
    print("               The word you must guess has {} letters.".format(round(len(letters_to_display)/2)))
    print("\n",myst_word,"\n\n")
    print("\t",end='')
    for each in letters_to_display:
        print(each,end='')
    print("\n")
    return letters_to_display # --------------------- TEST --------------------
    print("\t",end='')
    for each in mwl:
        print("_ ",end='')
    print("\t\t*** You have {} guesses left. ***".format(guesses_left))
    print("\n\n")
    print(" "*5,"Guesses so far: ",end='')
    for each in all_guesses:
        print(each," ",end='')
    print("\n")
    return


def get_guess(all_guesses):
    while True:
        entry = input("\n Guess a letter: ").lower()
        if validate_guess(entry):
            if entry not in all_guesses:
                all_guesses.append(entry)
                return entry
            print("\n***** You already guessed that letter  -  try again *****")


def check_guess(g, mwl):
    position_of_corr = []
    for index, each in enumerate(mwl):
        if each == g:
            position_of_corr.append(index)
    return position_of_corr


def change_display_letters(guess, letters_to_display, position_of_corr):
    for each in position_of_corr:
        pos = each * 2
        letters_to_display.insert(pos,guess)
        letters_to_display.pop(pos+1)


def did_you_win(letters_to_display):
    for each in letters_to_display:
        if each == "#":
            win = False
            return win
    win = True
    return win


def end(winner, myst_word):
    if winner:
        print("\n"*50)
        print("*"*60)
        print("\t\t       YOU WON !!!!!")
        print("*"*60)
        print("\n\n\n\n\n")
    else:
        print("\n"*50)
        print("-"*40)
        print("\t   Sorry, you lost")
        print("-"*40)
        print("\n\tThe word was:  {} ".format(myst_word))
        print("\n\n")

    ask = input("--- Would you like to play again? (y/n) ")
    if ask == 'y' or ask == 'Y':
        return True
    print("\n\n")
    return False


def validate_guess(entry):
    if len(entry) > 1:
        return False
    if entry not in 'abcdefghijklmnopqrstuvwxyz':
        return False
    return True


def get_word_list():
    word_list = []
    with open('/usr/share/dict/words','r') as f:
        for line in f:
            word_list.append(line)
    return word_list

def easy_words(word_list):
    ew = []                              # ======== for test
    for each in word_list:
        if len(each) > 3 and len(each) < 7:
            ew.append(each)
    return ew

def medium_words(word_list):
    mw = []                               # ======== for test
    for each in word_list:
        if len(each) > 5 and len(each) < 9:
            mw.append(each)
    return mw

def hard_words(word_list):
    hw = []                               # ======== for test
    for each in word_list:
        if len(each) > 7:
            hw.append(each)
    return hw



#========================================================================

def main():

    alive = True
    play_again = True

    word_list = get_word_list()      #from file
    easy_words = []
    normal_words = []
    hard_words = []
    game_list = []

    for each in word_list:
        if len(each) > 4 and len(each) < 8:
            easy_words.append(each)
    for each in word_list:
        if len(each) > 6 and len(each) < 10:
            normal_words.append(each)
    for each in word_list:
        if len(each) > 8:
            hard_words.append(each)

    #global myst_word
    #global mwl
    #global all_guesses
    #global position_of_corr

    while play_again:
        print("\n"*50)
        print("#"*40)
        print("\t   WELCOME TO HANGMAN")
        print("#"*40)
        print("\n\n")

        game_list = word_difficulty(easy_words, normal_words, hard_words)

        myst_word = get_myst_word(game_list)
        myst_word = myst_word.lower()
        print(myst_word,end='')
        mwl = list(myst_word)
        mwl.pop()
        print(len(mwl))
        letters_to_display = []
        for each in mwl:
            letters_to_display.append('#')
            letters_to_display.append(' ')
        all_guesses = []
        position_of_corr = []
        guesses_left = 8
        extra_guess = False

        while alive:

            display_board(guesses_left, letters_to_display, myst_word, mwl, all_guesses)

            guess = get_guess(all_guesses)

            position_of_corr = check_guess(guess, mwl)

            change_display_letters(guess, letters_to_display, position_of_corr)

            winner = did_you_win(letters_to_display)
            if winner:
                break

            if position_of_corr == []:
                guesses_left -= 1

            if guesses_left <= 0:
                alive = False

        play_again = end(winner, myst_word)
        if play_again:
            alive = True


if __name__ == '__main__':
   main()
