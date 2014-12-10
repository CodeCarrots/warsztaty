"""
Prosta klasa reprezentująca posiłek składający się z dwóch innych
obiektów jadalnych.
"""

class Meal:
    def __init__(self, food_a, food_b):
        # TODO: zainicjuj obiekt przekazanymi wartościami

    def get_name(self):
        # TODO: zaimplementuj metodę zwracającą nazwę obiektu
        # składającą się z połączonych spójnikiem "i" nazw składowych
        # obiektów jadalnych (food_a i food_b)

    def get_calories(self):
        # TODO: zaimplementuj metodę zwracającą wartość energetyczną
        # całego posiłku (jako sumę kalorii składowych obiektów jadalnych)


if __name__ == '__main__':
    import food

    # proste testy
    apple = Food("Jablko", 70)
    carrot = Food("Marchewka", 80)

    podwieczorek = Meal(apple, carrot)

    print (podwieczorek.get_name())     # "Jablko i Marchewka"
    print (podwieczorek.get_calories()) # 150
