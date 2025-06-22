from scuola import Student, Teacher, Casa, Scuola, Person

# import voto
# importiamo un solo nome, che è il nome del modulo "voto", e poi accedo alle varie classi con la notazione voto.Voto, voto.Libretto

from voto.modello import Voto, Libretto
# importiamo più nomi indipendenti, Voto, Libretto

# from voto import *
# importa tutti i nomi in voto in maniera indipendente, Voto, Libretto, cfuTot


# Grifondoro
Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro",
                animale="civetta", incantesimo="Expecto Patronum")
Hermione = Student(nome="Hermione", cognome="Granger", eta=11, capelli="castani", occhi="castani", casa="Grifondoro",
                   animale="gatto", incantesimo="Wingardium Leviosa")
Ron = Student(nome="Ron", cognome="Weasley", eta=11, capelli="rossi", occhi="azzurri", casa="Grifondoro",
              animale="topo")
Neville = Student(nome="Neville", cognome="Paciock", eta=11, capelli="castani", occhi="castani", casa="Grifondoro",
                  animale="rospo")
Ginny = Student(nome="Ginny", cognome="Weasley", eta=10, capelli="rossi", occhi="castani", casa="Grifondoro",
                animale="gatto")
Sirius = Person(nome="Sirius", cognome="Black", eta=36, capelli="neri", occhi="grigi",
                casa="Grifondoro")  # Sirius non è ne studente ne professore ad Hogwarts
Remus = Teacher(nome="Remus", cognome="Lupin", eta=36, capelli="castani", occhi="verdi", casa="Grifondoro",
                materia="Difesa contro le arti oscure")
Minerva = Teacher(nome="Minerva", cognome="McGranitt", eta=70, capelli="neri", occhi="verdi", casa="Grifondoro",
                  materia="Trasfigurazione", incantesimo="Trasfigurazione Animale")
Albus = Teacher(nome="Albus", cognome="Silente", eta=115, capelli="argento", occhi="azzurri", casa="Grifondoro",
                materia="Preside")
Rubeus = Person(nome="Rubeus", cognome="Hagrid", eta=60, capelli="neri", occhi="neri",
                casa="Grifondoro")  # Rubeus non è ne studente ne professore ad Hogwarts
James = Person(nome="James", cognome="Potter", eta=23, capelli="neri", occhi="castani", casa="Grifondoro")
Lily = Person(nome="Lily", cognome="Evans", eta=23, capelli="rosso", occhi="verdi", casa="Grifondoro")
Fred = Student(nome="Fred", cognome="Weasley", eta=16, capelli="rossi", occhi="castani", casa="Grifondoro",
               animale="nessuno")
George = Student(nome="George", cognome="Weasley", eta=16, capelli="rossi", occhi="castani", casa="Grifondoro",
                 animale="nessuno")

# Serpeverde
Draco = Student(nome="Draco", cognome="Malfoy", eta=11, capelli="biondi", occhi="grigi", casa="Serpeverde",
                animale="nessuno")
Severus = Teacher(nome="Severus", cognome="Snape", eta=45, capelli="neri", occhi="neri", casa="Serpeverde",
                  materia="Pozioni", incantesimo="Sectumsempra")
Horace = Teacher(nome="Horace", cognome="Lumacorno", eta=65, capelli="brizzolati", occhi="verdi", casa="Serpeverde",
                 materia="Pozioni", )
Bellatrix = Person(nome="Bellatrix", cognome="Lestrange", eta=47, capelli="neri", occhi="neri",
                   casa="Serpeverde")  # Bellatrix non è ne studente ne professore ad Hogwarts
Lucius = Person(nome="Lucius", cognome="Malfoy", eta=42, capelli="biondi", occhi="grigi",
                casa="Serpeverde")  # Lucius non è ne studente ne professore ad Hogwarts
Narcissa = Person(nome="Narcissa", cognome="Malfoy", eta=41, capelli="biondi", occhi="azzurri",
                  casa="Serpeverde")  # Narcissa non è ne studente ne professore ad Hogwarts
Pansy = Student(nome="Pansy", cognome="Parkinson", eta=12, capelli="neri", occhi="castani", casa="Serpeverde",
                animale="nessuno")
Blaise = Student(nome="Blaise", cognome="Zabini", eta=12, capelli="neri", occhi="castani", casa="Serpeverde",
                 animale="nessuno")
Tom_Riddle = Student(nome="Tom", cognome="Riddle", eta=16, capelli="neri", occhi="neri", casa="Serpeverde",
                     animale="serpente", incantesimo="Avada Kedavra")

# Corvonero
Luna = Student(nome="Luna", cognome="Lovegood", eta=11, capelli="biondi", occhi="azzurri", casa="Corvonero",
               animale="nessuno")
Cho = Student(nome="Cho", cognome="Chang", eta=12, capelli="neri", occhi="castani", casa="Corvonero", animale="nessuno")
Gilderoy = Teacher(nome="Gilderoy", cognome="Allock", eta=33, capelli="biondi", occhi="azzurri", casa="Corvonero",
                   materia="Difesa contro le Arti Oscure", incantesimo="Oblivion")
Filius = Teacher(nome="Filius", cognome="Vitious", eta=150, capelli="bianchi", occhi="azzurri", casa="Corvonero",
                 materia="Incantesimi", incantesimo="Wingardium Leviosa")
Xenophilius = Person(nome="Xenophilius", cognome="Lovegood", eta=49, capelli="bianchi", occhi="azzurri",
                     casa="Corvonero")  # Xenophilius non è ne studente ne professore ad Hogwarts
Padma = Student(nome="Padma", cognome="Patil", eta=13, capelli="neri", occhi="castani", casa="Corvonero",
                animale="nessuno")
Michael = Student(nome="Michael", cognome="Corner", eta=13, capelli="neri", occhi="castani", casa="Corvonero",
                  animale="nessuno")

# Tassorosso
Cedric = Student(nome="Cedric", cognome="Diggory", eta=16, capelli="castani", occhi="grigi", casa="Tassorosso",
                 animale="nessuno")
Pomona = Teacher(nome="Pomona", cognome="Sprout", eta=60, capelli="grigi", occhi="castani", casa="Tassorosso",
                 materia="Erbologia")
Hannah = Student(nome="Hannah", cognome="Abbott", eta=12, capelli="biondi", occhi="azzurri", casa="Tassorosso",
                 animale="nessuno")
Ernest = Student(nome="Ernest", cognome="Macmillan", eta=13, capelli="biondi", occhi="castani", casa="Tassorosso",
                 animale="nessuno")
Susan = Student(nome="Susan", cognome=" Bones", eta=12, capelli="rossi", occhi="verdi", casa="Tassorosso",
                animale="nessuno")
Ted = Person(nome="Ted", cognome="Tonks", eta=24, capelli="castano", occhi="neri",
             casa="Tassorosso")  # Ted non è ne studente ne professore ad Hogwarts

print(Harry, Ron, Susan, Xenophilius, Remus)

personaggi = [Harry, Hermione, Ron, Neville, Ginny, Sirius, Remus, Minerva, Albus, Rubeus, James, Lily, Fred, George,
              Draco, Severus, Horace, Bellatrix, Lucius, Narcissa, Pansy, Blaise, Luna, Cho, Gilderoy, Filius,
              Xenophilius, Padma, Michael, Cedric, Pomona, Hannah, Ernest, Susan, Ted]

grifondoro = Casa("Grifondoro", [])
tassorosso = Casa("Tassorosso", [])
corvonero = Casa("Corvonero", [])
serpeverde = Casa("Serpeverde", [])

print(grifondoro)

for p in personaggi:
    # if p.casa == grifondoro.nome & isinstance(p, Student):
    #     grifondoro.addStudente(p)
    # if p.casa == tassorosso.nome & isinstance(p, Student):
    #     tassorosso.addStudente(p)
    # if p.casa == corvonero.nome & isinstance(p, Student):
    #     corvonero.addStudente(p)
    # if p.casa == serpeverde.nome & isinstance(p, Student):
    #     serpeverde.addStudente(p)
    if isinstance(p,Student):
        match p.casa:
            case "Grifondoro":
                grifondoro.addStudente(p)
            case "Tassorosso":
                tassorosso.addStudente(p)
            case "Corvonero":
                corvonero.addStudente(p)
            case "Serpeverde":
                serpeverde.addStudente(p)
            case _:
                print(f"Jumping {p}")

print(grifondoro)

v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
v2 = Voto("Pozioni", 30, "2022-02-17", True)
v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
print(v1)
print()

mylib = Libretto(Harry, [v1, v2])
print(mylib)
mylib.append(v3)
print(mylib)


# print(Lily._cognome) # NOO!
# print(Lily._Person__prova) NOOOOOOO!
