# -*- coding: utf-8 -*-

'''Statystyka liter
'''

# http://www.prezydent.pl/prezydent/priorytety#nowoczesny_patriotyzm
TEXT = """
W opinii Prezydenta RP patriotyzm – pozostając miłością Ojczyzny i troską o jej bezpieczeństwo – przejawia się w budowaniu nowoczesnego państwa, w działaniach obywatelskich na rzecz regionu oraz miejsca, w którym mieszkamy i pracujemy. Osiągnięcia 25-lat wolności kształtują poczucie dumy z sukcesu Polski. Dla Bronisława Komorowskiego szczególne znaczenie mają zaplanowane na cały 2014 rok inicjatywy, które będą przypominały światu, że przemiany demokratyczne w Europie Środkowo-Wschodniej i upadek komunizmu miały początek właśnie w Polsce.
"""
# http://budapest.hu/Lapok/default.aspx
#TEXT = '''
#A városvezetés kész tervekkel rendelkezik a ciklusra; elfogadták Budapest új városfejlesztési koncepcióját, a területfejlesztési koncepciót, a kerületekkel közösen megalkották a tematikus fejlesztési programokat, elkészült az új, integrált településfejlesztési stratégia, elfogadták a közlekedésfejlesztésről szóló Balázs Mór-terv egyeztetési változatát, a Duna-menti területek fejlesztési tanulmánytervét, valamint szintén elkészült a Margitsziget fejlesztési koncepciója.
#'''
# http://www.insse.ro/cms/ro/content/prezentare-generala
#TEXT = '''
#Statistica  oficiala  în  România  se  desfasoara  prin  serviciile  de  statistica oficiala  si  este   organizata  si  coordonata  de  Institutul  National de Statistica, organ  de  specialitate  al  administratiei  publice  centrale,  cu  personalitate juridica, în subordinea Guvernului, finantat de la bugetul de stat.
#'''

def main():
    statystyka = {}
#    index = 0
#    while index < len(TEXT):
#        znak = TEXT[index]
#        index += 1

#    for [...] in [...]:
#        [...]
    for znak in TEXT:
        if znak in statystyka:
            statystyka[znak] += 1
#            statystyka[znak] = statystyka[znak] + 1
        else:
            statystyka[znak] = 1

#    print(statystyka)

    wyjscie = list(statystyka.items())

    print('lista surowa:', wyjscie)
    
    wyjscie.sort()

#    print('lista posortowana:', wyjscie)

    print('lista posortowana:')
#    for element in wyjscie:
#        znak = element[0]
#        ilosc = element[1]
    for znak, ilosc in wyjscie:
        print('litera: {0}, ilość: {1}'.format(znak, ilosc))

    rewers = []
    for znak, ilosc in wyjscie:
        rewers.append( (ilosc, znak) )

    rewers.sort()
    rewers.reverse()

    print('--------------------------------')

    print('lista posortowana po ilośći, malejąco:')
    for ilosc, znak in rewers:
        print('litera: {0}, ilość: {1}'.format(znak, ilosc))



if __name__ == '__main__':
    main()


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
