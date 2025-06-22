import operator
from dataclasses import dataclass

from dao.dao import LibrettoDAO
from voto.voto import Voto

cfuTot = 180

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti
        #self.dao = LibrettoDAO() non creo un'istanza perché è una classe stateless
        self.fillLibretto()

    def fillLibretto(self):
        allEsami = LibrettoDAO.getAllVoti()
        for e in allEsami:
            self.append(e) # metodo che c'è qui sotto

    def append(self, voto): # duck!
        if (self.hasVoto(voto) is False and self.hasConflitto(voto) is False):
            self.voti.append(voto)
            if not LibrettoDAO.hasVoto(voto):
                LibrettoDAO.addVoto(voto)
        else:
            raise ValueError("Il voto è già presente")

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    def __len__(self):
        return len(self.voti)

    def calcolaMedia(self):
        """
        restituisce la media dei voti attualmente presenti nel libretto
        :return: valore numerico della media, oppure ValueError in caso la lista fosse vuota
        """
        # v = []
        # for v1 in self.voti:
        #     v.append(v1.punteggio)
        # equivale a :
        if len(self.voti) == 0:
            raise ValueError("Attenzione, lista esami vuota.")
        else:
            v = [v.punteggio for v in self.voti]
            # math.mean(v)
            return sum(v)/len(v)

    def getVotiByPunti(self, punti, lode):
        """
        restituisce una lista di esami con punteggio uguale a punti (e lode se applicata)
        :param punti: variabile di tipo intero che rappresenta il punteggio
        :param lode: booleano che indica se è presente la lode
        :return: lista di voti
        """
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode:
                votiFiltrati.append(v)
        return votiFiltrati

    def getVotoByName(self, nome):
        """
        restituisce un oggetto Voto il cui campo materia è uguale a nome
        :param nome: stringa che indica il nome della materia
        :return: oggetto di tipo Voto, oppure None in caso di voto non trovato
        """
        for v in self.voti:
            if v.materia == nome:
                return v

    def hasVoto(self, voto):
        """
        verifica se il libretto contiene già il voto "voto"; due voti sono considerati uguali
        per questo metodo se hanno lo stesso campo materia e lo stesso campo punteggio
        (voto è formato da due campi: punteggio e lode)
        :param voto: istanza dell'oggetto di tipo Voto
        :return: True se il voto è presente, False altrimenti
        """
        for v in self.voti:
            # modo numero 1
            # if v == voto:   in questo caso, senza aver definito __eq__, dovrei passare lo stesso riferimento per avere True
            #     pass

            # modo numero 2
            if voto.materia == v.materia and voto.punteggio == v.punteggio and voto.lode == v.lode:
                return True
        return False

    def hasConflitto(self, voto):
        """
        questo metodo controlla che il voto "voto" non rappresenti un conflitto con i
        voti già presenti nel libretto; consideriamo due voti in conflitto quando hanno lo
        stesso campo materia ma diversa coppia punteggio-lode
        :param voto: instanza della classe Voto
        :return: True se il voto è in conflitto, False altrimenti
        """
        for v in self.voti:
            if (v.materia == voto.materia and not (v.punteggio == voto.punteggio and v.lode == voto.lode)):
                return True
        return False

    def copy(self):
        """
        crea una nuova copia del libretto
        :return: instanza della classe Libretto
        """
        nuovo = Libretto(self.proprietario.copy(), [])
        for v in self.voti:
            nuovo.append(v.copy())
        # così in nuovo non ho gli stessi riferimenti del libretto originario
        # nuovo = Libretto(self.proprietario.copy(), self.voti.copy.deepcopy())
        return nuovo

    def creaMigliorato(self):
        """
        crea un nuovo oggetto Libretto, in cui i voti sono migliorati secondo la seguente
        logica:
        se il voto è >= 18 e < 24, aggiungo +1
        se il voto è >= 24 e < 29, aggiungo +2
        se il voto è 29 aggiungo +1
        se il voto è 30 rimane 30
        :return: nuovo Libretto
        """
        nuovo = self.copy()
        # modifico i voti
        for v in nuovo.voti:
            if 18 <= v.punteggio < 24:
                v.punteggio = v.punteggio + 1
            elif 24 <= v.punteggio < 29:
                v.punteggio = v.punteggio + 2
            elif v.punteggio == 29:
                v.punteggio = 30
        return nuovo

    def sortByMateria(self):
        # self.voti.sort(key=estraiMateria)
        self.voti.sort(key=operator.attrgetter("materia"))

    # Opzione 1: creo due metodi di stampa, che ordinano e poi stampano
    # Opzione 2: creo due metodi che ordinano la lista di self e poi un unico metodo che stampa
    # Opzione 3: creo due metodi che si fanno una copia autonoma della lista (deep copy), la ordinano, e la restituiscono
    #            poi un altro metodo si occuperà di stampare le liste
    # Opzione 4: creo una shallow copy di self.voti e ordino quella

    def creaLibOrdinatoPerMateria(self):
        """
        crea un nuovo oggetto Libretto e lo ordina per materia
        :return: nuova insanza dell'oggetto Libretto
        """
        nuovo = self.copy()
        nuovo.voti.sort(key=estraiMateria)
        return nuovo

    def creaLibOrdinatoPerVoto(self):
        """
        crea un nuovo oggetto Libretto e lo ordina per voto
        :return: nuova insanza dell'oggetto Libretto
        """
        nuovo = self.copy()
        nuovo.voti.sort(key = lambda v: (v.punteggio, v.lode), reverse=True)
        #True>False di default
        return nuovo

    def cancellaInferiori(self, punteggio):
        """
        questo metodo agisce sul libretto corrente, eliminando tutti i voti inferiori al parametro punteggio
        :param punteggio: intero indicante il valore minimo
        :return:
        """
        # Modo 1
        # for i in range(len(self.voti)):
        #     if self.voti[i].punteggio < punteggio:
        #         self.voti.pop(i)
        # non va bene perché itero una lista che sta cambiando, salto alcuni voti

        # Modo 2
        # for v in self.voti:
        #     if v.punteggio < punteggio:
        #         self.voti.remove(v)
        # non va bene

        # Modo 3
        nuovo = []
        for v in self.voti:
            if v.punteggio >= punteggio:
                nuovo.append(v)
        self.voti = nuovo

        # scrittura compatta:
        # nuovo = [v for v in self.voti if v.punteggio >= punteggio]


def estraiMateria(voto):
    """
    questo metodo restituisce il campo materia dell'oggetto voto
    :param voto: instanza della classe Voto
    :return: stringa rappresentante il nome della materia
    """
    return voto.materia


def testVoto():
    print("Ho usato Voto in maniera standalone")
    print()
    v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
    print(v1)
    print()
    mylib = Libretto(None, [v1, v2])
    print(mylib)
    mylib.append(v3)
    print(mylib)

if __name__ == "__main__":   # solo nel caso in cui eseguo modello.py, esegue testVoto(): se eseguo il main NO (__name__ = voto)
    testVoto()