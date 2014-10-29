Kamień, nożyczki, papier ...
========================
W pliku knp_final.py znajduje się działająca wersja gry "Kamień, nożyczki, papier". Jednak to nie znaczy, że jest to już wersja ostateczna. Spróbuj zaprogramowac przynajmniej jedno z poniższych rozszerzeń.
Rozszerzenie 1. 
---------------
###... Lizard, Spock

Rock, paper, scissors, lizard, Spock to rozszerzona wersja gry, która zawiera dwie nowe gesty. Dokładny opis gry znajduje sie [tutaj](http://pl.wikipedia.org/wiki/Papier,_kamie%C5%84,_no%C5%BCyce,_jaszczurka,_Spock).

Główne zadanie polega na tym, żeby wymyśleć sposób na uproszczenie logiki sprawdzającej kto wygrał. W final_knp.py wygląda to następująco:

```
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
Można oczywiście dopisać w podobny sposób kolejne warunki. Zadziała? Zadziała.
Ale można zrobić to znacznie prościej. 
#### Podpowiedź: 
Jeżeli z odpowiedzi gracza i odpowiedzi komputera zrobimy napis to jakie napisy będą świadczyły o zwycięstwie komputera?

Rozszerzenie 2.
---------------
### Walidacja wejścia czyli sprawdź co wpisał gracz.
Progran final_knp.py ma pewne ułomności w logice.
Jeżeli na pytanie o wybór gestu gracz wprowadzi inna odpowiedź niż "k", "n" albo "p" to źle zostanie obliczone kto wygrał grę. Podobnie zresztą sprawa wygląda z pytaniem o to czy kontynuujemy grę. Jeżeli gracz poda cokolwiek innego niż "t" to gra sie nie skończy.

Dodaj sprawdzanie czy gracz podał prawidłową odpowiedź. Jeżeli nie, to ponawiaj pytanie dopóki gracz nie udzieli prawidłowej odpowiedzi.

Rozszerzenie 3. 
---------------
### Statystyka gry
Granie graniem, ale dobrze byłoby wiedzieć ile razy kto wygrał. W ramach tego rozszerzenia możesz wprowadzić następujące modyfikacje:
* oprócz informacji o tym kto wygrał dana rozgrywkę można podawać informację o tym ile dotychczas gier wygrał komputer a ile gracz nie-komputer.
* można zmienić kryteria zakończenia programu usuwając pytanie o to czy gramy dalej, ale w zamian przerywając grę po np. 10 rozgrywkach, na końcu podając ile razy kto wygrał.
* dla prawdziwych entuzjastów: można zapisywać statystyki w pliku przy zakończeniu gry i raczyć nimi gracza po uruchomieniu gry ("Hej, komputer wygrał z Tobą 123123425662222238 razy w kamień, nożyczki, papier. Na pewno chcesz grac znowu?")

Jeżeli chodzi o zapis do pliku to można zrobić to normalnie zapisując do pliku dwie liczby (i nie zapominając o konwersjach liczb do formatu napisowego). Można również użyć biblioteki [pickle](https://docs.python.org/3.4/library/pickle.html)


Rozszerzenie 4. 
---------------
### Kombinujący komputer.
My możemy sie zastanowic który gest wybrać, ale biedny komputer nie, bo jak na razie zwyczajnie losuje. W ramach tego rozszerzenia możesz napisać fukncję, która pozwoli komputerowi trochę sprytniej wybierać gest analizując wyniki dotychczasowych gier. 
Przykładowy sposób "rozumowania" komputera może byc np. taki:
* jeżeli gracz przegrał poprzednia grę, to pewnie w tej pokaże inny gest niz w poprzedniej. Trzeba więc losować nie z trzech możliwości, ale z dwóch pozostałych.

