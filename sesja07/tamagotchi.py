import time
import random


# maksyalny czas spania Tamagotchi
MAX_SLEEP_TIME = 7

# okres aktywności (w sekundach) po którym Tamagotchi będzie
# potrzebować snu
CYCLE_TIME = 25

# maksymalna ilość energii przyswajalna w jednym posiłku
MAX_EAT_ENERGY = CYCLE_TIME


class Tamagotchi:
    """
    Klasa implementująca prostego Tamagotchi
    """


    def __init__(self, name):
        """
        Konstruktor klasy Tamagotchi
        """

        self.name = name
        self.feed_time = time.time()
        self.sleep_time = 0
        self.stored_energy = 0


    def is_hungry(self):
        """
        Funkcja sprawdza czy Tamagotchi głodny.
        Jeżeli od ostatniego karmienia upłynęło więcej czasu niż
        wartość pożywienia w brzusiu to oznacza, że głodny
        """

        if time.time() - self.feed_time > self.stored_energy:
            return True
        return False


    def is_tired(self):
        """
        Funkcja sprawdza czy Tamagotchi jest zmęczony.
        Jeżeli od ostatniego spania upłynęło więcej czasu niż
        pewna ustalona ilość sekund - wtedy jest zmęczony.
        """

        if time.time() - self.sleep_time > CYCLE_TIME:
            return True
        return False


    def get_name(self):
        return self.name


    def print_status(self):
        """
        Wypisuje status: imię, czy głodny, czy zmęczony
        """

        print("Imię:", self.get_name())
        print("Głodny?", self.is_hungry())
        print("Zmęczony?", self.is_tired())


    def eat(self, food):
        """
        Metoda do karmienia Tamagotchi.
        Jeżeli jest zmęczony to nie je.
        Jeżeli dostanie coś innego niż "food" to nie je.
        Jeżeli dostanie coś innego niż marchewka to nie je.
        Jeżeli dostanie marchewkę to:
        -jeżeli jest głodny to aktualizuje licznik jedzenia i czas karmienia
        -jeżeli nie jest głodny to aktualizuje tylko licznik jedzenia.
        Tamagotchi nie przyswoi więcej energii niż pewna określona ilość.
        """

        if self.is_tired():
            print("Nu-uuu...")
        elif not is_food(food):
            print("Hhhmmmm...?")
        elif 'marchewka' not in str(food.get_name()).lower():
            print("Bleeee!")
        else:
            sound = "Omnomnom <3"
            if self.is_hungry():
                self.stored_energy = 0
                self.feed_time = time.time()

            calories = food.get_calories()

            if calories > MAX_EAT_ENERGY:
                sound = "OOO...OOMMNooom...nomnom <3"
                calories = MAX_EAT_ENERGY

            self.stored_energy += calories
            print(sound)

    def sleep(self):
        """
        Funkcja do układania Tamagotchi do snu.
        Działa kiedy jest zmęczony.
        """

        if not self.is_tired():
            print("BUuAaaaaaa... T_T")
            return

        print("Zzzzz...")
        time.sleep(random.randint(1, MAX_SLEEP_TIME))

        self.sleep_time = time.time()

        print(r'\o/')


# funkcja sprawdzająca czy dany obiekt "implementuje" żądany interfejs
def is_food(food):
    return (callable(getattr(food, 'get_name', False)) and
            callable(getattr(food, 'get_calories', False)))


if __name__ == '__main__':
    # utwórz przykładowego tamagotchi i zobacz jak się ma...
    tini = Tamagotchi('Tini')
    tini.print_status()
