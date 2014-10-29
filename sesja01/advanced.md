Kamień, nożyczki, papier ...
============================

W pliku knp_final.py znajduje się działająca wersja gry "Kamień,
nożyczki, papier". Jednak to nie znaczy, że jest to już wersja
ostateczna. Spróbuj zaprogramować przynajmniej jedno z poniższych
rozszerzeń.


... Lizard, Spock
-----------------

Rock, paper, scissors, lizard, Spock to rozszerzona wersja gry, która
zawiera dwie nowe gesty. Dokładny opis gry znajduje się
[tutaj](http://pl.wikipedia.org/wiki/Papier,_kamie%C5%84,_no%C5%BCyce,_jaszczurka,_Spock).

Główne zadanie polega na tym, żeby wymyślić sposób na uproszczenie
logiki sprawdzającej kto wygrał. W final_knp.py wygląda to
następująco:

```python
# porownujemy symbole
if player_choice == "k" and computer_choice == "n":
    # kamien (gracz) vs nozyczki (komputer) = wygrywa kamien (czyli gracz)
    player_victory = True
elif player_choice == "n" and computer_choice == "p":
    # nozyczki (gracz) vs papier (komputer) = wygrywaja nozyczki
    player_victory = True
elif player_choice == "p" and computer_choice == "k":
    # papier (gracz) vs kamien (komputer) = wygrywa papier
    player_victory = True
```

Można oczywiście dopisać w podobny sposób kolejne warunki. Zadziała?
Zadziała.  Ale można zrobić to znacznie prościej.

#### Podpowiedź

Jeżeli z odpowiedzi gracza i odpowiedzi komputera zrobimy napis to
jakie napisy będą świadczyły o zwycięstwie komputera?


Walidacja wejścia czyli sprawdź co wpisał gracz
-----------------------------------------------

Program final_knp.py ma pewne ułomności w logice.  Jeżeli na pytanie o
wybór gestu gracz wprowadzi inna odpowiedź niż "k", "n" albo "p" to
źle zostanie obliczone kto wygrał grę. Podobnie zresztą sprawa wygląda
z pytaniem o to czy kontynuujemy grę. Jeżeli gracz poda cokolwiek
innego niż "t" to gra się nie skończy.

Dodaj sprawdzanie czy gracz podał prawidłową odpowiedź. Jeżeli nie, to
ponawiaj pytanie dopóki gracz nie udzieli prawidłowej odpowiedzi.


Statystyka gry
--------------

Granie graniem, ale dobrze byłoby wiedzieć ile razy kto wygrał. W
ramach tego rozszerzenia możesz wprowadzić następujące modyfikacje:
* oprócz informacji o tym kto wygrał dana rozgrywkę można podawać
  informację o tym ile dotychczas gier wygrał komputer a ile gracz
  nie-komputer.
* można zmienić kryteria zakończenia programu usuwając pytanie o to
  czy gramy dalej, ale w zamian przerywając grę po np. 10 rozgrywkach,
  na końcu podając ile razy kto wygrał.
* dla prawdziwych entuzjastów: można zapisywać statystyki w pliku przy
  zakończeniu gry i raczyć nimi gracza po uruchomieniu gry ("Hej,
  komputer wygrał z Tobą 123123425662222238 razy w kamień, nożyczki,
  papier. Na pewno chcesz grac znowu?")

Jeżeli chodzi o zapis do pliku to można zrobić to normalnie zapisując
do pliku dwie liczby (i nie zapominając o konwersjach liczb do formatu
napisowego). Można również użyć biblioteki
[pickle](https://docs.python.org/3.4/library/pickle.html).


Kombinujący komputer
--------------------

My możemy się zastanowić który gest wybrać, ale biedny komputer nie,
bo jak na razie zwyczajnie losuje. W ramach tego rozszerzenia możesz
napisać funkcję, która pozwoli komputerowi trochę sprytniej wybierać
gest analizując wyniki dotychczasowych gier.  Przykładowy sposób
"rozumowania" komputera może być np. taki:
* jeżeli gracz przegrał poprzednia grę, to pewnie w tej pokaże inny
  gest niż w poprzedniej. Trzeba więc losować nie z trzech możliwości,
  ale z dwóch pozostałych.


Podziel się wiedzą
------------------

Gdybyśmy chcieli rozszerzyć nasz program o obsługę
[większej ilości "broni"](http://en.wikipedia.org/wiki/Rock-paper-scissors#Additional_weapons)
zwiększy się również ilość wygrywających kombinacji. Aby przeciętny
gracz nie musiał się trudnić zapamiętywaniem tych wszystkich
informacji możesz rozszerzyć program w taki sposób żeby po każdej
rundzie przedstawiał graczowi wszystkie ruchy które w danej rundzie
mogły komputer pokonać (np.: "Wybrałem kamień: papier zawija kamień,
Spock dezintegruje kamień...").
