# init
krotka = ()
krotka = tuple()
krotka = tuple([1, 2, 3])
krotka = tuple((1, 2, 3))
krotka = (1)                # ???
krotka = (1,)               # !!!
krotka = 1, 2, 3, 4

krotka2 = tuple(krotka)     # !!!

krotka2 = (1,) * 10
krotka2 = tuple("AndNowForSomethingCompletelyDifferent...")

zbior = {}                  # ???
zbior = {1, 2, 3, "test"}   # !!!
zbior = set()
zbior = set([])
zbior = set(['a', 1, (1,1), (1,2), (1,1), "test", False])
zbior = set(set((1, 2, 3)))

lista = []
lista = list()
lista = list([])
lista = [1, 2, 3, True, (1,), {1, 2}]
lista = list([1, 2, 3, True, (1,), {1, 2}])
lista = list(list([1, 2, 3, True, (1,), {1, 2}]))

slownik = {}
slownik = dict()
slownik = dict({})
slownik = {1: 2, 2: 1}
slownik = {'a': 2, 'b': 1, (1, 1): "trafiony!", (1, 2): "pudło!"}
slownik = dict(a=2, b=1)



# get one
krotka[0]
krotka[-1]
krotka[-2]
krotka2[-20]

zbior.pop()

lista[0]
lista[-1]
lista[-2]
lista[-5]

slownik['a']



# add/set one
krotka = krotka + (1, )
krotka += (1, )

zbior.add(1)
zbior.add(2)

lista.append([1])
lista.extend([1])

slownik['aaa'] = 1
slownik[False] = 2
slownik[(1, 1)] = 2
slownik.setdefault(1, '4')



# drop one
zbior.pop()
zbior -= set([1])

lista.pop()
lista.pop(0)
del lista[0]

slownik.pop('b')
slownik.popitem()



# split (disjoin)

# iterable[:index] + iterable[index:] == iterable

a = krotka[0:2]
b = krotka[2:]

a = lista[0:2]
b = lista[2:]
lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista[0:-1:2]


# concatenate / join / add many
krotka += (1, [1, 2, 3])        # ???

zbior.update(zbior)
zbior = zbior.union([1, 2, 5])

lista.append([1, 2, 3])
lista.extend([5, 6, 7])
lista += [9, 8 ,7]

slownik.update(slownik)


# copy all
zbior.copy()                    # ???

slownik.copy()                  # ???

lista[:]
lista[::]

import copy


# TBD:
# - operatory na przykładach
# - iteracje i użycie metody obiektów na przykładach

