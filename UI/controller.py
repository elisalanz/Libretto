from scuola import Student
from UI.view import View
from voto.modello import Libretto
from voto.voto import Voto
import flet as ft


class Controller:
    def __init__(self, v:View):
        self._view = v
        self._student = Student("Harry", "Potter", 11, "castani", "azzurri", "Grifondoro", "civetta", "Expecto Patronum")
        self._model = Libretto(self._student, [])

    def handleAggiungi(self, e):
        #Raccoglie tutte le ifno per creare un nuovo voto
        #Crea un oggetto Voto
        #Fa append sul libretto
        nome = self._view._txtInNome.value
        if nome == "":
            self._view._txtOut.controls.append(ft.Text("Attenzione. Il campo nome non può essere vuoto", color = "red"))
            self._view._page.update()
            return
        punti = self._view._ddVoto.value
        if punti is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione. Selezionare un voto", color="red"))
            self._view._page.update()
            return
        data = self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione. Selezionare una data", color="red"))
            self._view._page.update()
            return
        if punti == "30L":
            self._model.append(Voto(nome, 30, f"{data.year}-{data.month}-{data.day}", True))
        else:
            self._model.append(Voto(nome, int(punti), f"{data.year}-{data.month}-{data.day}", False))
        self._view._txtOut.controls.append(ft.Text("Voto correttamente aggiunto", color = "green"))
        self._view._page.update()

    def handleStampa(self, e):
        self._view._txtOut.controls.append(ft.Text(str(self._model), color = "black"))
        self._view._page.update()


    def getStudent(self):
        """
        Restituisce informazioni dello studente usando il __str__ dell'oggetto Student
        :return:
        """
        return str(self._student)

