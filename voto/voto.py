# class Voto:
#     def __init__(self, materia, punteggio, data, lode):
#         if  punteggio == 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = lode
#         elif punteggio < 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = False
#         else:
#             raise ValueError(f"Attenzione, non posso creare un voto con punteggio {punteggio}")
#     def __str__(self):
#         if self.lode:
#             return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
#         else:
#             return f"In {self.materia} hai preso {self.punteggio} il {self.data}"


from dataclasses import dataclass


@dataclass(order=True)
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    def copy(self):
        return Voto(self.materia, self.punteggio, self.data, self.lode)

    # def __eq__(self, other):
    #     if self.materia == other.materia and self.punteggio == other.punteggio:
    #         return True
    #     else:
    #         return False
    #     # return (self.punteggio == other.punteggio and self.lode == lode and self.materia == other.materia)

    def __eq__(self, other):
        return self.materia == other.materia

    def __hash__(self):
        return hash(self.materia)
