# -*- coding: utf-8 -*-

'''
Klon gry Mastermind oparty na "frameworku"
'''

# Funkcje frameworkowe z implementacja zasad gry Mastermind

def getMaxNumberOfGuesses():
    return 10


def getGuessCount():
    return 3


def getRiddleSet():
    return "RBGY"


def printGameDescription():
    print("Mastermind: gra polega na odgadnięciu %s-literowego kodu składającego się z liter %s." % (
        getGuessCount(),
        getRiddleSet(),
    ))
    print("Masz na to %s prób(y)." % getMaxNumberOfGuesses())


def getRiddle():
    riddle = ""
    for i in range(getGuessCount()):
        riddle += random.choice(getRiddleSet())
#    riddle = ''.join(random.choice(getRiddleSet())
#        for _ in range(getGuessCount()))
#    print ("Riddle: ", riddle)
    return riddle


def getUserGuess():
    return input("Podaj kod: ")


def evaluateGuess(riddle, player_choice):
    if riddle == player_choice:
        return True
    else:
        correct_place = 0
        correct_not_in_place = 0
        for i in range(getGuessCount()):
            if riddle[i] == player_choice[i]:
                correct_place += 1
            elif player_choice[i] in riddle:
                    correct_not_in_place += 1
        print ("Prawidłowe miejsce: ", correct_place)
        print ("Kod jest ale w innym miejscu: ", correct_not_in_place)


def printCongratulations(riddle):
    print("Gratulacje! Zgadłeś kod. Kod to:", riddle)


def validateGuess(user_guess):
    correct_chars = True
    for letter in user_guess:
        if letter not in getRiddleSet():
            correct_chars = False
    if len(user_guess) == getGuessCount() and correct_chars:
        return True
    else:
        print ("Nieprawidłowa odpowiedź.")
        return False

# gra wlasciwa

import random

printGameDescription()
# flaga kontynuacji gry: True = gramy (kolejna) runde
keep_playing = True
max_guesses = getMaxNumberOfGuesses()

# glowna petla gry
while keep_playing:
    riddle = getRiddle()
    riddle_guessed = False
    guess = 0
    while guess < max_guesses and not riddle_guessed:
        print ("Proba: ", guess + 1)
        user_guess_valid = False
        while not user_guess_valid:
            user_guess = getUserGuess()
            user_guess_valid = validateGuess(user_guess)
        riddle_guessed = evaluateGuess(riddle, user_guess)
        guess += 1

    # sprawdzamy czy gra sie skonczyla, bo wyczerpala sie ilosc prob
    # czy dlatego, ze gracz zgadl
    if riddle_guessed:
        printCongratulations(riddle)
    else:
        print("Nie ma więcej prób. Przegrałeś :(")

    # zapytanie o kontynuacje gry
    next_game = input("Jeszcze jedna zagadka (T/n)?")
    if next_game == "n":
        # nie, konczymy...
        keep_playing = False


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
