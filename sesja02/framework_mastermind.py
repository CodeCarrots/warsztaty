'''
Gra w mastermind, ale w powiedzmy "frameworku"
'''

# Funkcje frameworkowe z implementacja masterminda

def gameDescription():
    print ("MasterMind: gra polega na odgadnieciu trzyliterowego kodu skladajacego sie z liter R, G, B lub Y.")
    print ("Masz na to 10 prob.")

def createRiddle():
    riddle = ""
    for i in list(range(3)):
        riddle = riddle + random.choice("RBGY")
    print ("Riddle: ", riddle)
    return riddle

def userGuessPrompt():
    return input("Podaj kod: ")

def evaluateGuess(riddle, player_choice):
    if riddle_guessed == player_choice:
        return True
    else:
        correct_place = 0
        correct_not_in_place = 0
        for i in list(range(3)):
            if riddle[i] == player_choice[i]:
                correct_place = correct_place + 1
            elif player_choice[i] in riddle:
                    correct_not_in_place = correct_not_in_place + 1
        print ("Prawidlowe miejsce: ", correct_place)
        print ("Kod jest ale w innym miejscu: ", correct_not_in_place)


def congratulate(riddle) :
    print("Gratulacje! Zgadles kod. Kod to ", riddle)


def getMaxNumberOfGuesses() :
    return 10

def validateGuess(user_guess):
    correct_chars = True
    for letter in user_guess:
        if letter not in "RBGY":
            correct_chars = False
    if len(user_guess) == 3 and correct_chars:
        return True
    else:
        print ("Neprawidlowa odpowiedz.")
        return False

# gra wlasciwa

import random

gameDescription()
# flaga kontynuacji gry: True = gramy (kolejna) runde
keep_playing = True
max_guesses = getMaxNumberOfGuesses()

# glowna petla gry
while keep_playing:
    #glowna petla
    riddle = createRiddle()
    riddle_guessed = False
    guess = 0
    while guess < max_guesses and not riddle_guessed:
        print ("Proba: ", guess + 1)
        user_guess_valid = False
        while not user_guess_valid:
            user_guess = userGuessPrompt()
            user_guess_valid = validateGuess(user_guess)
        riddle_guessed = evaluateGuess(riddle, user_guess)
        guess = guess + 1

    #sprawdzamy czy gra sie skonczyla, bo wyczerpala sie ilosc prob
    #czy dlatego, ze gracz zgadl
    if riddle_guessed:
        congratulate()
    else:
        print("Nie ma wiecej prob. Przegrales :(")
    # zapytanie o kontynuacje gry
    next_game = input("Jeszcze jedna zagadka (T/n)?")

    if next_game == "n":
        # tak, konczymy...
        keep_playing = False

