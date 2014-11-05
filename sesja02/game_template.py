'''Szablon z zarysem prostego "framework'u" dla tworzenia prostych gier.
'''

##
# jeżeli używamy dodatkowych modułów to zaimportujmy je tutaj
# ...


##
# definicje funkcji i zmiennych globalnych powinny znaleźć się tutaj
# ...


##
# kod głównej pętli gry
#

printGameDescription()
# flaga kontynuacji gry: True = gramy (kolejna) runde
keep_playing = True
max_guesses = getMaxNumberOfGuesses()

# główna pętla gry
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
