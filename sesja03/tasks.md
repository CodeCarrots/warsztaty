Zadania
=======

Statystyka liter
----------------

Statystyka znaków stworzona poprzez zliczanie z użyciem tzw. kubełków. Każdej literze odpowiada oddzielny licznik. Można zacząć z zainicjalizowanymi licznikami (kubełkami) dla całego zakładanego *alfabetu* lub bez.

Końcowa statystyka powinna zostać przedstawiona dwojako:

- w porządku alfabetycznym względem liter;
- w porządku malejącym względem ilości liter;

Przykładowe teksty można znaleźć w pliku [letters_stat.py](./letters_stat.py).


K-N-P-L-S
---------

Korzystając rozszerzenia klasycznej wersji gry kamień-nożyczki-papier zawartego w opisie [sesji nr 01](../sesja01/advanced.md#-lizard-spock) spróbuj zaimplementować metodę sprawdzającą wynik pojedynczej rozgrywki bez użycia *drabinki* warunków sprawdzających. Proponowane sposoby wyznaczania wygranego w K-N-P-L-S:

- mapowanie grup wyników - ustalamy, które kombinacje wyborów *(użytkownik, komputer)* dają wygraną użytkownika/komputera i na tej podstawie wyświetlamy wynik; przykładowe rozwiązanie przy pomocy listy/zbioru i krotek;
- mapowanie + matematyka - odpowiednio mapując broń na wartości i przeprowadzając proste obliczenia możemy wyznaczyć zwycięzcę :)


Wisielec
--------

Zadaniem jest implementacja klasycznej wersji gry [Wisielec](http://pl.wikipedia.org/wiki/Wisielec_%28gra%29) przy pomocy szablonu z [sesji nr 02](../sesja02).

W skrócie: dajemy użytkownikowi 7 (siedem) prób na odgadnięcie hasła. Każda nieudana próba to dodatkowy element rysunku "wisielca". Cały rysunek oznacza koniec gry i przegraną gracza. Słowo jest losowane ze słownika - dla uproszczenia (?) można przyjąć, że słowa są tylko rzeczownikami - albo tylko angielskimi albo polskimi, nie zawierającymi polskich liter.

Konieczne jest zaimplementowanie co najmniej:

- warunku ilości prób;
- wyświetlania użytych liter i wykonywania testów w celu uniknięcia podawania ponownie tej samej litery;
- wyświetlania podglądu odgadywanego słowa;
- testu odgadnięcia (słowo powinno zostać wprowadzone celem weryfikacji przez komputer).

Procedura rysująca na ekranie (konsoli) tytułowego wisielca została zaimplementowana i zostanie omówiona na zajęciach.


Detekcja języka
---------------

Mamy prosty detektor działający z następującymi językami:

- czeski
- niemiecki
- hiszpański
- węgierski
- włoski
- polski
- rumuński
- turecki

Celem jest *zgadnięcie* języka na podstawie tekstu źródłowego i zestawów znaków diakrytycznych. Założenie upraszczające: badamy tylko znaki charakterystyczne dla danego języka. *(Czy to zasadne czy trzeba byłoby coś jeszcze sprawdzać?)*

Przykładowy sposób rozwiązania: kubełkowanie + wybieranie najliczniejszej reprezentacji. Zakładamy, że nasz program działa w trybie offline ;)


Sekwencje DNA
-------------

Celem zadania jest poprawne wyszukiwanie, zliczanie i rekodowanie wybranych par/kombinacji zasad z ciągu wejściowego (przykład niżej) oraz przekonwertowanie go do tzw. notacji IUPAC przy jednoczesnej próbie skrócenia końcowego zapisu.

Przykładowa sekwencja wejściowa w formacie tekstowym:

```
ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC
CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC
CTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG
AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCC
CTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG
TTTAATTACAGACCTGAA
```

Mapa podstawień:

- A = adenina
- C = cytozyna
- G = guanina
- T = tymina
- U = uracyl
- R = G A (puryna)
- Y = T C (pirymidyna)
- K = G T (keton)
- M = A C (amin)
- S = G C
- W = A T
- B = G T C
- D = G A T
- H = A C T
- V = G C A
- N = A G C T (inne)

Trudność optymalizacji polega na takim dobieraniu podstawienia z *mapy* aby uzyskać nie tylko jednoznaczny ciąg wyjściowy ale także aby był on najkrótszy. Przykładowo: fragment `GA` w ciągu wejściowym można zastąpić przez `R` ale jeśli `GA` poprzedza bezpośrednio `T` właściwszym jest użycie podstawienia `GAT` -> `D` zamiast `GAT` -> `RT`.
