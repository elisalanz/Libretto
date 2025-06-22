from scuola import Student
from voto.modello import Libretto, Voto

Harry = Student("Harry", "Potter", 11, "castani", "azzurri", "Grifondoro","civetta", "Expecto Patronum")
myLib = Libretto(Harry, [])

v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 21, "2022-02-12", False)
myLib.append(v1)
myLib.append(v2)
myLib.append(Voto("Pozioni", 21, "2022-06-14", False))
myLib.append(Voto("Trasfigurazione", 21, "2022-06-14", False))

media = myLib.calcolaMedia()
print(media)

votiFiltrati = myLib.getVotiByPunti(21, False)
print(votiFiltrati)
#print(votiFiltrati[0])

votoTrasfigurazione = myLib.getVotoByName("Trasfigurazione")
if votoTrasfigurazione == None:
    print("Voto non trovato")
else:
    print(votoTrasfigurazione)

print(myLib.hasVoto(v1))
print(myLib.hasVoto(Voto("Aritmanzia", 30, "2023-07-10", False)))
print(myLib.hasVoto(Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)))
print(myLib.hasConflitto(Voto("Difesa contro le arti oscure", 21, "2022-01-30", False)))

print("Test append modificata")
myLib.append(Voto("Aritmanzia", 30, "2023-07-10", False)) # tutto OK
# myLib.append(Voto("Difesa contro le arti oscure", 21, "2022-01-30", False)) # errore, funziona

myLib.append(Voto("Divinazione", 27, "2021-02-08", False))
myLib.append(Voto("Cura delle creature magiche", 26, "2021-06-14", False))

print("----------------------")
print("Libretto originario")
print(myLib)

nuovoLib = myLib.creaMigliorato()
print("Libretto migliorato")
print(nuovoLib)
print("Libretto originario")
print(myLib)

print("----------------------")
ordinato = myLib.creaLibOrdinatoPerMateria()
print("Libretto ordinato per materia")
print(ordinato)

print("----------------------")
ordinato2 = myLib.creaLibOrdinatoPerVoto()
print("Libretto ordinato per voto")
print(ordinato2)

print("----------------------")
print("Libretto a cui ho eliminato i voti inferiori a 24")
ordinato2.cancellaInferiori(24)
print(ordinato2)