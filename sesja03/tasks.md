Zadania
=======

Statystyka liter
----------------

Statystyka znaków stworzona poprzez zliczanie z użyciem tzw. kubełków.
Każdej literze odpowiada oddzielny licznik. Można zacząć z zainicjalizowanymi
licznikami (kubełkami) lub bez.


K-N-P-L-S
---------

Szybkie wyznaczanie wygranego w K-N-P-L-S:

- mapowanie grup wyników - ustalamy, które kombinacje wyborów
  *(użytkownik, komputer)* dają wygraną użytkownika/komputera i na tej podstawie
  wyświetlamy wynik; przykładowe rozwiązanie przy pomocy listy/zbioru i krotek;
- mapowanie + matematyka - odpowiednio mapując broń na wartości
  i przeprowadzając proste obliczenia możemy wyznaczyć zwycięzcę :)


Wisielec
--------

Dajemy użytkownikowi 7 (siedem) prób na odgadnięcie hasła. Każda nieudana próba
to dodatkowy element rysunku "wisielca". Cały rysunek oznacza koniec gry
i przegraną gracza. Słowo jest losowane ze słownika - dla uproszczenia (?)
można przyjąć, że słowa są tylko rzeczownikami - albo tylko angielskimi albo
polskimi, nie zawierającymi polskich liter.


Detekcja języka
---------------

Język:

- czeski
- niemiecki
- hiszpański
- węgierski
- włoski
- polski
- rumuński
- turecki

*Zgadywanie* języka na podstawie tekstu źródłowego i zestawów znaków
diakrytycznych. Założenie upraszczające: badamy tylko znaki charakterystyczne
dla danego języka. *(Czy to zasadne czy trzeba byłoby coś jeszcze sprawdzać?)*

Przykładowy sposób rozwiązania: kubełkowanie + wybieranie najliczniejszej
reprezentacji.


Sekwencje DNA
-------------

Wyszukiwanie, zliczanie i rekodowanie wybranych par/kombinacji zasad do notacji
IUPAC.

Przykładowa sekwencja w formacie tekstowym:

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
- N = A G C T (any)

