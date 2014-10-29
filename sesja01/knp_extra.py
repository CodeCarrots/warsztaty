'''Gra w kamień-nożyczki-papier

(gdyby ten moduł eksportował użyteczne zewnętrznie dane lub funkcje to
krótka ich dokumentacja mogłaby się znaleźć tutaj)
'''

##
# w pierwszej kolejności importujemy moduły z których będziemy
# korzystać w naszym programie:

import random


##
# definicje funkcji i zmiennych globalnych (m.in. np. tabel
# opisujących logikę/strategię, itp.) powinny znaleźć się tutaj
# ...

##
# gdybyśmy chcieli zachowywać pewne informacje pomiędzy uruchomieniami
# programu tu byłoby dobre miejsce na wczytanie takich danych...

##
# następnie - miejsce na sedno programu
#
# tu zakładamy że chcemy rozegrać szereg gier / rund - realizujemy to
# w najprostszej postaci poprzez bezpośrednią pętlę z prostym
# warunkiem

# flaga kontynuacji gry: True = gramy (kolejnę) rundę
keep_playing = True

# główna pętla gry
while keep_playing:
    ##
    # dane wejściowe dla bieżącej rundy
    # wczytanie ruchu gracza:
    player_choice = input("[k]amień, [n]ożyczki, [p]apier? ")

    ##
    # czas na wybór ruchu komputera
    #
    # zaimplementowana strategia to "wybór losowy", ale moglibyśmy
    # próbować robić coś ciekawszego...
    computer_choice = random.choice("knp")

    ##
    # przedstawienie stanu gry
    #
    # prezentacja dokonanych wyborów symboli, powinniśmy w zasadzie
    # tłumaczyć ruchy na czytelną dla gracza postać, a nie tylko "k",
    # "n", "p"...
    print("Ty wybrałeś", player_choice)
    print("Ja wybrałem", computer_choice)

    ##
    # miejsce na implementację logiki gry - dla KNP, w najprostszej
    # wersji porównujemy wybory graczy i sprawdzamy który ruch był
    # lepszy

    # flaga wygranej gracza
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

    ##
    # mając wynik / zwycięzcę, pora na przedstawienie wyniku użytkownikowi
    if player_victory:
        print("Wygrałeś!")
    else:
        print("Wygrałem, yay! :P")

    ##
    # jedna rozgrywka / runda zakończona
    #
    # w tym miejscu moglibyśmy umieścić kod odpowiedzialny za dane
    # wspólne dla serii rozgrywek, czyli np. zliczanie statystyk, itp...
    #

    ##
    # musimy również obsłużyć kwestię wyjścia z pętli głównej

    # zapytanie o kontynuację gry
    finish_game = input("Koniec gry (t/n)? ")

    # czy kończymy?
    if finish_game == "t":
        # tak, kończymy...
        keep_playing = False

##
# seria rozgrywek (w pętli głównej) zakończona - miejsce na ewentualne
# wyświetlenie informacji podsumowujących oraz zachowanie stanu
# gdybyśmy chcieli śledzić pewne informacje poprzez szereg wywołań
# programu...
