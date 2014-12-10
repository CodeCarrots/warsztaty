"""
Prosta klasa reprezentująca posiłek składający się z wielu innych
obiektów jadalnych.
"""

class BigMeal:
    def __init__(self, edibles):
        # TODO: zainicjuj obiekt przekazaną listą obiektów jadalnych
        # "edibles"

    def get_name(self):
        # TODO: zaimplementuj metodę zwracającą nazwę obiektu
        # składającą się z połączonych spójnikiem "i" nazw wszystkich
        # składowych obiektów jadalnych

    def get_calories(self):
        # TODO: zaimplementuj metodę zwracającą wartość energetyczną
        # całego posiłku (jako sumę kalorii składowych obiektów jadalnych)


if __name__ == '__main__':
    import food

    # proste testy
    apple = Food("Jablko", 70)
    carrot = Food("Marchewka", 80)
    banana = Food("Banan", 60)

    fruitmix = BigMeal([apple, carrot, banana])
    print (fruitmix.get_name())     # "Jablko i Marchewka i Banan"
    print (fruitmix.get_calories()) # 210
