Liczbowe "ciepło-zimno"
=======================

Bazując na wiedzy i kodzie z sesji01 napisać prostą grę w której gracz
musi zgadnąć liczbę wybraną przez komputer (z dowolnego przedziału,
np. 1-99) gdy ma na to zadaną liczbę prób a po każdej nieudanej próbie
program podpowiada czy zgadywana liczba jest większa czy mniejsza od
tej wybranej przez program.


Gier ciąg dalszy...
===================

W pliku [game_template.py](./game_template.py) znajduje się
niedokończona wersja kodu, która może być użyta do napisania prostych
gier, podobnych do tych które pisaliśmy do tej pory. Główna brakująca
część to funkcje implementujące logikę danej gry.


Mastermind
----------

Korzystając z szablonu, bez modyfikacji istniejącego w pliku kodu
pętli głównej, poprzez dodanie brakującego kodu - głównie definicji
funkcji - zaimplementować grę
[Mastermind](http://pl.wikipedia.org/wiki/Mastermind_%28gra_planszowa%29).

Do reprezentacji pionków kolorów można użyć pojedynczych liter,
np. "R", "G", "B" i "Y" (czyli przykładowy ukryty kod mógłby być
przedstawiony jako ciąg znakowy "RGRY")


Wisielec
--------

Korzystając z szablonu zaimplementować grę
[Wisielec](http://pl.wikipedia.org/wiki/Wisielec_%28gra%29). Postaraj
się napisać kod tak aby gracz nie mógł podawać tej samej litery w
kilku próbach.
