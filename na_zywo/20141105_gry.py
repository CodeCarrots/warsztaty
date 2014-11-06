import random

def get_player_choice(prompt, valid_choices):
    while True:
        answer = input(prompt)
        if answer in valid_choices:
            return answer
        else:
            print("Zły wybór, spróbuj jeszcze raz.")

def guess_number():
    guess_min = 1
    guess_max = 99

    attempts_left = 10

    computer_choice = random.randint(guess_min, guess_max)

    while True:
        prompt = "Zgadnij liczbę ({0} do {1}, pozostało prób: {2}): "
        answer = input(prompt.format(guess_min, guess_max, attempts_left))
        player_choice = int(answer)

        print("Ty wybrałeś", player_choice)

        if player_choice < computer_choice:
            print("Za mało.")
        elif player_choice > computer_choice:
            print("Za dużo.")
        else:
            print("Zgadłeś, gratuluję!")
            break

        attempts_left -= 1
        if attempts_left <= 0:
            print("Nie udało się - pomyślana liczba to:", computer_choice)
            break

def knp():
    bad_choice = True

    player_choice = get_player_choice("Podaj swój ruch: [k]amień, [n]ożyczki, [p]apier? ", ["k", "n", "p"])

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


while True:
    answer = get_player_choice("W co chcesz zagrać? [C]iepło-zimno czy [K]np? [Z]akończ? ", ["c", "k", "z"])

    if answer == "c":
        guess_number()
    elif answer == "k":
        knp()
    elif answer == "z":
        break

print("Dzięki, zapraszam ponownie.")
