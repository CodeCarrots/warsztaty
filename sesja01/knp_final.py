'''Gra w 
'''

import random

# flaga kontynuacji gry: True = gramy (kolejna) runde
keep_playing = True

# glowna petla gry
while keep_playing:
    # gracz podaje swoj symbol
    player_choice = input("[k]amień, [n]ożyczki, [p]apier?")
    # komputer losuje wlasny symbol
    computer_choice = random.choice("knp")
    # prezentacja dokonanych wyborow symboli
    print("Ty wybrałeś", player_choice)
    print("Ja wybrałem", computer_choice)

    # flaga wygranej komputera
    player_victory = False

    # porownujemy symbole
    if player_choice == "k" and computer_choice == "n":
        # kamien (gracz) vs nozyczki (komputer) = wygrywa kamien (czyli gracz)
        player_victory = True
    elif player_choice == "n" and computer_choice == "p":
        # nozyczki (gracz) vs papier (komputer) = wygrywaja nozyczki
        player_victory = True
    elif player_choice == "p" and computer_choice == "k":
        # papier (gracz) vs kamien (komputer) = wygrywa papier
        player_victory = True

    # prezentacja zwyciezcow
    if player_victory:
        print("Wygrałeś!")
    else:
        print("Wygrałem, yay! :P")

    # zapytanie o kontynuacje gry
    finish_game = input("Koniec gry (t/n)?")

    # czy konczymy?
    if finish_game == "t":
        # tak, konczymy...
        keep_playing = False
