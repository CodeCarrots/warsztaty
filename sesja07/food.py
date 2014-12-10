"""
Prosta klasa reprezentująca obiekt jadalny o dwóch cechach: nazwa
i wartość energetyczna (kalorie).
"""

class Food:
    def __init__(self, name, calories):
        # TODO: zainicjuj obiekt przekazanymi wartościami

    def get_name(self):
        # TODO: zaimplementuj metodę zwracającą nazwę "name" obiektu

    def get_calories(self):
        # TODO: zaimplementuj metodę zwracającą wartość energetyczną
        # danego obiektu


if __name__ == '__main__':
    # proste testy
    apple = Food("Jablko", 70)

    print (apple.get_name())     # "Jablko"
    print (apple.get_calories()) # 70
