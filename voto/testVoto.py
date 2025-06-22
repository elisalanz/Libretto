from modello import Libretto
from voto.voto import Voto

v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
v2 = Voto("Pozioni", 30, "2022-02-17", True)
v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
print(v1)

mylib = Libretto(None, [v1, v2])
print(mylib)
mylib.append(v3)
print(mylib)

# questo è un altro modo per testare il modulo voto