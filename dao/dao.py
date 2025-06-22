# import mysql.connector

from dao.dbConnect import DBConnect
from voto.voto import Voto


class LibrettoDAO:
    # def __init__(self):
    #     self.dbConnect = DBConnect()   # è un classmethod non c'è bisogno di istanziarlo!

    @staticmethod
    def getAllVoti():  # non gli passo il parametro self
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "root",
        #     host = "127.0.0.1",
        #     database = "libretto",
        # )
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from voti"""
        cursor.execute(query)

        res = []
        for row in cursor:
            materia = row["materia"]
            punteggio = row["punteggio"]
            if row["lode"] == "False":
                lode = False
            else:
                lode = True
            data = row["data"].date()  # .date() per togliere informazioni inutili sull'orario
            v = Voto(materia, punteggio, data, lode)
            res.append(v)

        cnx.close()
        return res

    @staticmethod
    def addVoto(voto: Voto):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "root",
        #     host = "127.0.0.1",
        #     database = "libretto",
        # )
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor()
        query = "insert into voti (materia, punteggio, data, lode) values (%s, %s, %s, %s)"  # %s perché non conosco i valori
        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))  # eccoli
        cnx.commit() # per modificare database!!!!!
        cnx.close()
        return

    @staticmethod
    def hasVoto(voto: Voto):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "root",
        #     host = "127.0.0.1",
        #     database = "libretto",
        # )
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor()
        query = """select * from voti where materia = %s"""
        cursor.execute(query, (voto.materia,))  # passo una tupla anche se ha un solo argomento
        res = cursor.fetchall()
        cnx.close()
        return len(res) > 0 # significa che il voto c'è


if __name__ == "__main__":
    mydao = LibrettoDAO()
    print(mydao.getAllVoti())
