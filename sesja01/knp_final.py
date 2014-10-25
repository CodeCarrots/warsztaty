import random

keep_playing = True

while keep_playing:
    player_choice = input("[k]amień, [n]ożyczki, [p]apier?")
    computer_choice = random.choice("knp")
    print("Ty wybrałeś", player_choice)
    print("Ja wybrałem", computer_choice)

    player_victory = False

    if player_choice == "k" and computer_choice = "n":
    	player_victory = True
    elif player_choice == "n" and computer_choice = "p":
    	player_victory = True
    elif player_choice == "p" and computer_choice = "k":
    	player_victory = True

    if player_victory:
    	print("Wygrałeś!")
    else:
    	print("Wygrałem, yay! :P")

    finish_game = input("Koniec gry (t/n)?")

    if finish_game == "t":
        keep_playing = False
