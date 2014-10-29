import random

keep_playing = True

while keep_playing:
    bad_choice = True

    while bad_choice:
        player_choice = input("Podaj swój ruch: [k]amień, [n]ożyczki, [p]apier? ")

        if player_choice == "k":
            bad_choice = False
        elif player_choice == "n":
            bad_choice = False
        elif player_choice == "p":
            bad_choice = False
        else:
            print("Zły wybór, jeszcze raz?")

    computer_choice = random.choice(["k", "n", "p"])

    print("Ty wybrałeś", player_choice)
    print("Ja wybrałem", computer_choice)


    player_victory = False

    if player_choice == "k" and computer_choice == "n":
        player_victory = True
    elif player_choice == "n" and computer_choice == "p":
        player_victory = True
    elif player_choice == "p" and computer_choice == "k":
        player_victory = True

    if player_choice == computer_choice:
        print("Remis.")
    elif player_victory:
        print("Wygrałeś, gratuluję!")
    else:
        print("Ja wygrałem.")

    player_answer = input("Gramy dalej [t/n]? ")
    if player_answer == "n":
        keep_playing = False
